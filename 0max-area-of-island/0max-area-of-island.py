class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_valid(row, col):
            return (0 <= row < m) and (0 <= col < n) and grid[row][col] == 1
        
        def dfs(row, col, seen):
            
            seen[row][col] = True
            area = 1
            
            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx 
                if is_valid(next_row, next_col) and not seen[next_row][next_col]:
                    area += dfs(next_row, next_col, seen)

            return area
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        seen = [ [False] * n for _ in range(m)]
        
        max_area = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and not seen[row][col]:
                    curr_area = dfs(row, col, seen)
                    max_area = max(max_area, curr_area)
                    
        return max_area