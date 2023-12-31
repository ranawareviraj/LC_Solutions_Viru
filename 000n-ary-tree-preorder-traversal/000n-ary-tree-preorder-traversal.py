"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node, result):
            if not node:
                return []
            
            cur_result = [node.val]
            
            for child in node.children:
                cur_result.extend(dfs(child, cur_result))
            
            return cur_result
            
        return dfs(root, [])