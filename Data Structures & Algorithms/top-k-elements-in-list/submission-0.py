import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        heap = []
        for item in count:
            heapq.heappush(heap, [count[item], item])
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        
        result.reverse()
        return result