"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level = []
            
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    level.append(node.val)

                for child in node.children:
                    queue.append(child)
                
            ans.append(level)
        
        return ans
                
                

        
