class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for u, v in edges:
                if u == node:
                    nei = v
                elif v == node:
                    nei = u
                else:
                    continue
                
                if nei == parent:
                    continue

                if nei in visited:
                    return False

                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n