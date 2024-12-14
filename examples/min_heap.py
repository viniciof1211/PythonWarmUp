import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    def push(self, val):
        heapq.heappush(self.heap, val)
    def pop(self):
        return heapq.heappop(self.heap)
    def is_empty(self):
        return len(self.heap) == 0