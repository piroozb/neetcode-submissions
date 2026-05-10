from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i, j, 0])
        
        visited = set()
        while queue:
            r, c, level = queue.popleft()
            if (r, c) not in visited:
                visited.add((r, c))
                if grid[r][c] != -1 and grid[r][c] != 0:
                    grid[r][c] = level
                if r + 1 < len(grid) and grid[r + 1][c] != -1:
                    queue.append([r + 1, c, level + 1])
                if r - 1 >= 0 and grid[r - 1][c] != -1:
                    queue.append([r - 1, c, level + 1])
                if c + 1 < len(grid[0]) and grid[r][c + 1] != -1:
                    queue.append([r, c + 1, level + 1])
                if c - 1 >= 0 and grid[r][c - 1] != -1:
                    queue.append([r, c - 1, level + 1])