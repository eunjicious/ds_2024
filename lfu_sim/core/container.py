from enum import Enum

class NodeIndexEnum(Enum):
    PARENT = 0
    LEFT_CHILD = 1
    RIGHT_CHILD = 2


def enum_index_mapper(type: NodeIndexEnum, index: int) -> int:
    if type == NodeIndexEnum.PARENT:
        return (index - 1) // 2
    return 2 * index + type.value


class MinHeap(list):
    @property
    def size(self):
        return len(self)    
    
    def heappush(self, data):
        current = self.size
        self.append(data)
        while current > 0:
            parent = enum_index_mapper(NodeIndexEnum.PARENT, current)
            if self[parent] <= self[current]:
                break
            self[current], self[parent] = self[parent], self[current]
            current = parent


    def heappop(self):
        target = self[0]
        last = self.pop()
        if self.size == 0:
            return target
        self[0] = last
        current = 0
        while True:
            left_child = enum_index_mapper(NodeIndexEnum.LEFT_CHILD, current)
            right_child = enum_index_mapper(NodeIndexEnum.RIGHT_CHILD, current)
            if left_child >= self.size: 
                return target

            child = right_child if right_child < self.size and self[right_child] < self[left_child] else left_child
            
            if self[current] <= self[child]:
                return target
            
            self[child], self[current] = self[current], self[child]
            current = child


if __name__ == "__main__":
    heap = MinHeap()
    heap.heappush(4)
    heap.heappush(10)
    heap.heappush(1)
    heap.heappush(100)
    heap.heappush(0)
    heap.heappush(-123)
    heap.heappush(20)

    while heap:
        print(heap.heappop())    
