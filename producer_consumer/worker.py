from listQueue import ListQueue
import threading
import time

class Producer:
    def __init__(self, items):
        pass

    def get_item(self):
        pass

    def run(self):
        pass

    def start(self):
        pass

    def finish(self):
        pass

class Consumer:
    def __init__(self):
        pass

    def run(self):
        pass

    def start(self):
        pass

    def finish(self):
        pass

if __name__ == "__main__":
    
    customers = []
    with open("customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    names = []
    for c in customers:
        names.append(c[1])

    producer = Producer(names)

    # Priority 
#    producer = Producer(customers)

    consumer = Consumer()    
    producer.start()
    consumer.start()
    time.sleep(10)
    producer.finish()
    consumer.finish()
