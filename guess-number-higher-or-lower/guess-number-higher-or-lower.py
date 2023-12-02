# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        ans = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            x = guess(mid)
            
            if x >= 0:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return ans