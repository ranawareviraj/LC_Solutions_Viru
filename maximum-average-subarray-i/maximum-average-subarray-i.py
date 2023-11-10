class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Fixed size sliding window
        # Build initial window of size k and compute its sum
        curr = 0
        for i in range(k):
            curr += nums[i]
        
        # Slide window one element at a time and update the answer
        ans = curr
        n = len(nums)
        for i in range(k, n):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)
        
        return ans / k
