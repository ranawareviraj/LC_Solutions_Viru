class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = -math.inf
        for key, val in count.items():
            if val == 1:
                ans = max(ans, key)
        
        return (-1 if ans == -math.inf else ans)