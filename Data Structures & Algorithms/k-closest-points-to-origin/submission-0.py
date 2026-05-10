import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for point in points:
            heapq.heappush_max(queue, (point[0] ** 2 + point[1] ** 2, point))
        while len(queue) > k:
            heapq.heappop_max(queue)
        
        return [item[1] for item in queue]
            