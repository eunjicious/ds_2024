class ListQueue(list):
	def enqueue(self, item) -> None:
		self.append(item)

	def dequeue(self):
		return self.pop(0)
	
	def isEmpty(self):
		return len(self) == 0
	
	def front(self):
		return self[0] if self else None

	def __str__(self) -> str:
		return " ".join(self)


class PriorityQueue(ListQueue):
	def __init__(self):
		super().__init__()

	def enqueue(self, x):
		cnt = 0
		for _ in range(len(self)):
			if self.front() >= x:
				super().enqueue(self.dequeue())
				cnt += 1
			else: break
		super().enqueue(x)
		for _ in range(len(self) - cnt - 1):	
			super().enqueue(self.dequeue())	