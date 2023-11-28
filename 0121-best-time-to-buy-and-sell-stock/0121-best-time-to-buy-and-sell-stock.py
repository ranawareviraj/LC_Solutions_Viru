class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = math.inf

        for curr_price in prices:
            min_price = min(min_price, curr_price)
            max_profit = max(max_profit, curr_price - min_price)
        
        return max_profit

        