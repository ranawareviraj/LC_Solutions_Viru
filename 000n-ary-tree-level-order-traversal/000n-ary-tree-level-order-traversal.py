"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        
        # BFS Queue
        queue = deque([])
        
        if root:
            queue.append(root)
        
        # BFS
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                
                for child in node.children:
                    queue.append(child)
            
            result.append(level)
        
        return result