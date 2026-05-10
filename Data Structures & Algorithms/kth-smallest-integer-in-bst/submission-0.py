# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_tree = []
        def inorder_traversal(curr):
            if curr:
                inorder_traversal(curr.left)
                sorted_tree.append(curr.val)
                inorder_traversal(curr.right)
        
        inorder_traversal(root)

        return sorted_tree[k - 1]
