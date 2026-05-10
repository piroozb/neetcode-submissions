# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque([[root, 0]])

        while queue:
            curr, level = queue.popleft()
            if curr:
                if level + 1 > len(res):
                    res.append([])
                res[level].append(curr.val)
                queue.append([curr.left, level + 1])
                queue.append([curr.right, level + 1])

        return res
