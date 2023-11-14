class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        curr_weight = 0
        MAX_WEIGHT = 5000
        number_of_apples = 0
        
        for apple in weight:
            if curr_weight + apple <= MAX_WEIGHT:
                number_of_apples += 1
            else:
                break
            curr_weight += apple
        
        return number_of_apples
        