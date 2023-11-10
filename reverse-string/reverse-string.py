class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_string(s, left, right):
            if left > right:
                return
            
            s[left], s[right] = s[right], s[left]
            
            reverse_string(s, left + 1, right - 1)
            
        reverse_string(s, 0, len(s) - 1)
        
            