class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        ans = 0 
        seen = defaultdict(int)
        
        for right in range(n):
            seen[s[right]] += 1
            while len(seen) < right - left + 1:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    seen.pop(s[left])
                left += 1
            
            ans = max(ans, len(seen))
        
        return ans