class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int longest = 0;
        Set<Character> seen = new HashSet<>();
        
        for(int right = 0; right < s.length(); right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left += 1;
            }
            seen.add(s.charAt(right));
            longest = Math.max(longest, right - left + 1);
        }
        
        return longest;
    }
}