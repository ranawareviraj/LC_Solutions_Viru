# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, minimum_so_far, max_so_far):
            if not node:
                return abs(minimum_so_far - max_so_far)
                        
            max_so_far = max(max_so_far, node.val)
            minimum_so_far = min(minimum_so_far, node.val)
            
            max_diff_in_left = dfs(node.left, minimum_so_far, max_so_far)
            max_diff_in_right = dfs(node.right, minimum_so_far, max_so_far)
                        
            return max(max_diff_in_left, max_diff_in_right) 
        
        return dfs(root, math.inf, -math.inf)