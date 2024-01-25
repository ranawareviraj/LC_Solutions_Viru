class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int curr = 0;
        int longestOnes = 0;
        
        for(int right = 0; right < nums.length; right++){
            curr += nums[right] == 0 ? 1 : 0;
            
            while(curr > k){
                curr -= nums[left] == 0 ? 1 : 0;
                left += 1;
            }
            
            longestOnes = Math.max(longestOnes, right - left + 1);
        }
        
        return longestOnes;
    }
}
