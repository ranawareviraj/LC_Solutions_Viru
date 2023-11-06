class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def backtrack(index, current_combination):
            if len(current_combination) == len(digits):
                combinations.append("".join(current_combination))
                return 
            
            current_digit = digits[index]
            letters_of_current_digit = letter_map[current_digit]
            
            for letter in letters_of_current_digit:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
            
        if len(digits) == 0:
            return []

        letter_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        combinations = []
        backtrack(0, [])
        return combinations