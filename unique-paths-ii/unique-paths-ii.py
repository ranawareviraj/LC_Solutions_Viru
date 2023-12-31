class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Base Case
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] != 1:
                    if r > 0 and obstacleGrid[r - 1][c] != 1:
                        dp[r][c] += dp[r - 1][c]
                    if c > 0 and obstacleGrid[r][c - 1] != 1:
                        dp[r][c] += dp[r][c - 1]
        return dp[m - 1][n - 1]
                            
                        