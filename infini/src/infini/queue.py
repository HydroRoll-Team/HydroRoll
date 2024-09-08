from infini.exceptions import KeyError
from infini.typing import Generic, T
from collections import deque

import heapq


class EventQueue(Generic[T]):
    heap: list
    entry_finder: dict
    counter: int
    order_queue: deque

    def __init__(self) -> None:
        self.heap = []
        self.entry_finder = {}
        self.counter = 0
        self.order_queue = deque()

    def push(self, priority: int, item: T) -> None:
        if item in self.entry_finder:
            self.remove(item)
        entry = [priority, self.counter, item]
        self.counter += 1
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)
        self.order_queue.appendleft(item)

    def pop(self) -> T:
        while self.heap:
            _, _, item = heapq.heappop(self.heap)
            if self.entry_finder[item] is not None:
                del self.entry_finder[item]
                self.order_queue.remove(item)
                return item
        raise KeyError("Event queue is empty.")

    def remove(self, item) -> None:
        entry = self.entry_finder.pop(item)
        entry[-1] = None

    def is_empty(self) -> bool:
        return not bool(self.heap)

    def generate(self):
        while not self.is_empty():
            yield self.pop()
