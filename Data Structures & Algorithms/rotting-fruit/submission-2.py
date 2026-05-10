from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
        
        visited = set()
        minutes = 0
        while queue:
            r, c, minutes = queue.popleft()
            if (r, c) not in visited:
                visited.add((r, c))
                if r + 1 < len(grid) and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    queue.append([r + 1, c, minutes + 1])
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    queue.append([r - 1, c, minutes + 1])
                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    queue.append([r, c + 1, minutes + 1])
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    queue.append([r, c - 1, minutes + 1])
        
        has_fresh = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    has_fresh = True
                    break
            if has_fresh:
                break

        return -1 if has_fresh else minutes

            
