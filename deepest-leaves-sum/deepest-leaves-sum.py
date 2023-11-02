# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # BFS queue
        queue = collections.deque([root])
        sum = 0

        while queue:
            n = len(queue)
            # Reset sum for each level
            sum = 0
            for _ in range(n):
                # Get the current node and add its val to current level sum
                node = queue.popleft()
                sum += node.val

                # Add next level onto queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        # At this point sum holds sum of last level   
        return sum 
        