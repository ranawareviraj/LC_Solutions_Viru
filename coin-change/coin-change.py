class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(target):
            if target == 0:
                return 0
            if target < 0:
                return math.inf
            
            ans = -1
            for coin in coins:
                remaining = target - coin
                remaining_coins = dp(remaining) + 1
                if ans == -1 or remaining_coins < ans:
                    ans = remaining_coins
            
            return ans
        result = dp(amount)
        return result if result != math.inf else -1
        