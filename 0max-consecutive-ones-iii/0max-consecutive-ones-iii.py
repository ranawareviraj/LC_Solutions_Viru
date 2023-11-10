class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        zeroes_count = 0
        max_consecutive_ones = 0
        
        for right in range(n):
            if nums[right] == 0:
                zeroes_count += 1
                
            while zeroes_count > k:
                if nums[left] == 0:
                    zeroes_count -= 1                
                left += 1
            
            max_consecutive_ones = max(max_consecutive_ones, right - left + 1)
        
        return max_consecutive_ones
            