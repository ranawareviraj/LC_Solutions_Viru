class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, memo = {}):
            # Base case
            if n <= 2:
                return n
            
            # Memo case
            if n in memo:
                return memo[n]
            
            # Recursive case
            memo[n] = dp(n - 1, memo) + dp(n - 2, memo)
            return memo[n]
    
        return dp(n)