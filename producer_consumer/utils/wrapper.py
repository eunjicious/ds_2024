class Customer:
    def __init__(self, priority: int, name: str):
        self.priority = priority
        self.name = name

    def __eq__(self, other: 'Customer') -> bool:
        return self.priority == other.priority

    def __lt__(self, other: 'Customer') -> bool:
        return self.priority < other.priority

    def __gt__(self, other: 'Customer') -> bool:
        return self.priority > other.priority

    def __le__(self, other: 'Customer') -> bool:
        return self.priority <= other.priority
    
    def __ge__(self, other: 'Customer') -> bool:
        return self.priority >= other.priority

    def __str__(self) -> str:
        return self.name
