class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        
        for ch in ransomNote:
            if ch not in counter:
                return False
            
            counter[ch] -= 1
            if counter[ch] == 0:
                counter.pop(ch) 
        
        return True