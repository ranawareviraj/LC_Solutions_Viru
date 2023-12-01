class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def find_next_greater_element(nums):
            n = len(nums)
            result = [-1] * n
            stack = []
            
            for i in range(n):
                while stack and nums[i] > nums[stack[-1]]:
                    j = stack.pop()
                    result[j] = nums[i]
                stack.append(i)
            
            return result
        
        index_map = defaultdict(int)
        m = len(nums1)
        for i, num in enumerate(nums2):
            index_map[num] = i
        
        next_greater_elements = find_next_greater_element(nums2)
        result = []
        for i, num in enumerate(nums1):
            index_in_nums2 = index_map[num]
            result.append(next_greater_elements[index_in_nums2])
        
        return result
            