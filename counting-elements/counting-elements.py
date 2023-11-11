class Solution:
    def countElements(self, arr: List[int]) -> int:
        elements = set(arr)
        count = 0
        
        for num in arr:
            if num + 1 in elements:
                count += 1
        
        return count