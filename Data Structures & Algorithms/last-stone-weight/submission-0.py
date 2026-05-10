import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = []
        for stone in stones:
            heapq.heappush_max(queue, stone)
        while len(queue) >= 2:
            y = heapq.heappop_max(queue)
            x = heapq.heappop_max(queue)
            if x == y:
                continue
            elif x < y:
                new_stone = y - x
                heapq.heappush_max(queue, new_stone)

        return queue[0] if queue else 0
