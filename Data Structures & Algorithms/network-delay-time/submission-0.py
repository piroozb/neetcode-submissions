import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        total_time = 0
        visited = set()

        queue = [(0, k)]

        while queue:
            time, u = heapq.heappop(queue)
            if u in visited:
                continue
            visited.add(u)
            for t in times:
                ui, vi, ti = t
                if ui == u:
                    if vi not in visited:
                        heapq.heappush(queue, (time + ti, vi))
            total_time = time
        
        return total_time if len(visited) == n else -1
