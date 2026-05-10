# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(curr, lowest, highest):
            if curr:
                if curr.val <= lowest or curr.val >= highest:
                    return False
                return dfs(curr.left, lowest, curr.val) and dfs(curr.right, curr.val, highest)
            return True

        return dfs(root, float('-inf'), float('inf'))