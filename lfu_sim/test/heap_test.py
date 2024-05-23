from core import MinHeap
import random

def test_heap_simple_sample():
    heap = MinHeap()
    for data in [1, 5, 2, 4, 0, 3, 6]:
        heap.heappush(data)
    result = []
    while heap:
        result.append(heap.heappop())
    assert result == sorted(result)


def test_heap_complex_sample():
    heap = MinHeap()
    SAMPLE_RANGE = (0, 100_000_000)
    SAMPLE_COUNT = 100_000
    sample = random.sample(range(*SAMPLE_RANGE), SAMPLE_COUNT)
    for data in sample:
        heap.heappush(data)
    result = []
    while heap:
        result.append(heap.heappop())
    assert result == sorted(result)