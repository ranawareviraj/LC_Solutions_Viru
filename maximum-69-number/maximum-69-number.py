class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        position_of_current_digit = 0
        position_of_first_six = -1
        while n > 0:
            if n % 6 == 0:
                position_of_first_six = position_of_current_digit
            
            n = n // 10
            position_of_current_digit += 1

        return (num if position_of_first_six == -1 
                    else num + 3 * 10 ** position_of_first_six) 
            