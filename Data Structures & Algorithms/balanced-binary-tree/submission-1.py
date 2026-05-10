# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
    
            return 1 + max(left, right)
        
        left = dfs(root.left)
        right = dfs(root.right)
        if left == right or left == right + 1 or left == right - 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False