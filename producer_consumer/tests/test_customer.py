from utils.wrapper import Customer
import random


def once_compare_customer():
    a, b = random.randint(-1000, 1000), random.randint(-1000, 1000)
    cus_a, cus_b = Customer(a, "a"), Customer(b, "b")
    assert (cus_a > cus_b) == (a > b)
    assert (cus_a < cus_b) == (a < b)
    assert (cus_a == cus_b) == (a == b)
    assert (cus_a != cus_b) == (a != b)
    assert (cus_a >= cus_b) == (a >= b)
    assert (cus_a <= cus_b) == (a <= b)

def test_compare_customer_10000_times():
    for _ in range(10000):
        once_compare_customer()