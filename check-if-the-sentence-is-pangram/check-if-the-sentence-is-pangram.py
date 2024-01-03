class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Build Frequency map
        char_freq = [0] * 26
        ord_a = ord('a')
        for ch in sentence:
            char_freq[ord(ch) - ord_a] += 1
        
        # If any character has freq == 0, its not Pangram
        for freq in char_freq:
            if freq == 0:
                return False
        
        # If we reach here, then we have all alphabets in the sentence - Pangram
        return True
            