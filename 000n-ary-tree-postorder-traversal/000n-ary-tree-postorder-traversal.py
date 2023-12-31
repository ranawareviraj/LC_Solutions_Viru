"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node, curr):
            if not node:
                return []
            
            result = []
            for child in node.children:
                result.extend(dfs(child, result))
            
            result.append(node.val)
            return result
        
        return dfs(root, [])