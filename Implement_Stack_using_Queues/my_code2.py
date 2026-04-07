from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)
        size = len(self.queue.items)
        for _ in range(size - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self) -> int:
        return self.queue.dequeue()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()
