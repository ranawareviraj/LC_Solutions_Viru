class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = ans = x
        
        while left <= right:
            root = left + (right - left) // 2
            num = root * root
            
            if num <= x:
                ans = root
                left = root + 1
            else:
                right = root - 1
        
        return ans