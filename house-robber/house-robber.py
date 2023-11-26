class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(house_index, memo = {}):
            # If this is the only house (first), rob it
            if house_index == 0:
                return nums[house_index]
            
            # If we have two houses, rob the house with more money
            if house_index == 1:
                return max(nums[0], nums[1])
            
            # If we have computed result previously (memoized), use it
            if house_index in memo:
                return memo[house_index]
            
            # At any house, we have two options:
            # Rob it => money at second last house + curr house
            # Dont rob it => money we had at prev house
            memo[house_index] = max(dp(house_index - 1), dp(house_index - 2) + nums[house_index])
            return memo[house_index]
            
        return dp(len(nums) - 1)
    