# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
            
        left_length = self.minDepth(root.left)
        right_length = self.minDepth(root.right)
        
        if not root.left:
            return 1 + right_length
        if not root.right:
            return 1 + left_length
        
        return 1 + min(right_length, left_length)