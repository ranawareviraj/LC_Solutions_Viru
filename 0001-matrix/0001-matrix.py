class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Helper function to check if given cell is valid
        def is_valid(row, col):
            return (-1 < row < m) and (-1 < col < n) and (result[row][col] == math.inf)

        m = len(mat)
        n = len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[0] * n for _ in range(m)]

        seen = [[False] * n for _ in range(m)]
        queue = deque([])
        # Add level zero onto queue, cells with val as 0
        level = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    result[row][col] = math.inf
                else:
                    queue.append((row, col))
                    seen[row][col] = True
        
        # Perfrom BFS starting from level 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                row, col = queue.popleft()
                if result[row][col] == math.inf:
                    result[row][col] = level

                # Add next level onto queue
                for dx, dy in directions:
                    next_row = row + dy
                    next_col = col + dx

                    if is_valid(next_row, next_col) and not seen[next_row][next_col]:
                        seen[next_row][next_col] = True
                        queue.append((next_row, next_col))
            
            level += 1
        
        return result