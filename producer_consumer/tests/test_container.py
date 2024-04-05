from utils.container import ListQueue, PriorityQueue
import random

# 내부 아이템 갯수
ITEM_COUNT = 100
# 최소 ~ 최대
MINIMUM = -10_000; MAXIMUM = 10_000
# 반복 횟수
ITERATION = 1_000


def make_list_queue():
    queue, lst = ListQueue(), []
    for _ in range(ITEM_COUNT):
        rand = random.randint(MINIMUM, MAXIMUM)
        queue.enqueue(rand)
        lst.append(rand)
    assert queue == lst

def test_list_queue_many_times():
    for _ in range(ITERATION):
        make_list_queue()



def make_priority_queue():
    priority_queue, lst = PriorityQueue(), []
    for _ in range(ITEM_COUNT):
        rand = random.randint(MINIMUM, MAXIMUM)
        priority_queue.enqueue(rand)
        lst.append(rand)
    assert priority_queue == sorted(lst, reverse=True)

def test_priority_queue_many_times():
    for _ in range(ITERATION):
        make_priority_queue()



