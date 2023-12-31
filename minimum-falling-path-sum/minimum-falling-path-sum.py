class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp[0] = matrix[0][:]
        directions = [-1, 0, 1]
        
        for r in range(1, m):
            for c in range(n):
                prev_sum = math.inf
                for dx in directions:
                    prev_col = c + dx
                    if 0 <= prev_col < n:
                        prev_sum = min(prev_sum, dp[r - 1][prev_col])
                dp[r][c] = matrix[r][c] + prev_sum
        
        return min(dp[m - 1])
                        