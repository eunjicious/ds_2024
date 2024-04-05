# import require library
import threading
import argparse
import time

# get queue container code
from utils.container import PriorityQueue, ListQueue 

# get Customer wrapper
from utils.wrapper import Customer

# get configuration
from config import CUSTOMERS_DATA
from config import PRODUCER_DELAY, CONSUMER_DELAY



# setting arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--priority", dest="use_priority", action="store_true")



class Producer:
    def __init__(self, items):
        self.__alive = True
        self.items = items
        self.worker = threading.Thread(target=self.run)

    def get_item(self):
        for item in self.items:
            yield item

    def run(self):
        for item in self.get_item():
            if not self.__alive:
                break
            time.sleep(PRODUCER_DELAY)
            with lock:
                shared_queue.enqueue(item)
            print("Arrived:", item)
        print("Producer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()



class Consumer:
    def __init__(self):
        self.__alive = True
        self.worker = threading.Thread(target=self.run)

    def run(self):
        while self.__alive:
            time.sleep(CONSUMER_DELAY)
            if shared_queue.isEmpty():
                break
            with lock:
                item = shared_queue.dequeue()
                print("Boarding:", item)
        print("Consumer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()



def get_customers_data():
    with open(CUSTOMERS_DATA, 'r') as file:
        lines = file.readlines()
        for line in lines:
            grade, name = line.split()
            yield (int(grade), name)



if __name__ == "__main__":
    # Get Running Arguments
    args = parser.parse_args()
    
    # Setting Consumers Data
    customers = []
    for grade, name in get_customers_data():
        customers.append(Customer(grade, name))

    # Lock & Priority 
    lock = threading.Lock()

    # Check Use Priority
    print()
    print("==========================")
    print("    Use Priority Queue" if args.use_priority else "    Not Priority Queue")
    print("==========================")
    print()
    
    shared_queue = ListQueue()
    if args.use_priority:
        shared_queue = PriorityQueue()
    
    # Setting Producer and Consumer Object
    producer = Producer(customers)
    consumer = Consumer()    
 
    # run main
    producer.start(); consumer.start()
    time.sleep(10)
    producer.finish(); consumer.finish()

