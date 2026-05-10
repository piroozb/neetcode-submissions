import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for point in points:
            heapq.heappush(queue, (point[0] ** 2 + point[1] ** 2, point))

        result = []
        while k > 0:
            dist, point = heapq.heappop(queue)
            result.append(point)
            k -= 1

        
        return result
            