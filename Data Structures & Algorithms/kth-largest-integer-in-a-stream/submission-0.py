import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = []
        self.k = k
        for num in nums:
            heapq.heappush(self.queue, num)
        
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]

        
