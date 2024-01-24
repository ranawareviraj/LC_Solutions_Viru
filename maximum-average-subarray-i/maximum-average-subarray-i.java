class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double currSum = 0;
        double maxSum = 0;
        
        for(int i = 0; i < k; i++){
            currSum += nums[i];
        }
        
        maxSum = currSum;
        
        for(int i = k; i < nums.length; i++){
            currSum -= nums[i - k];
            currSum += nums[i];
            maxSum = Math.max(maxSum, currSum);
        }
        
        return maxSum / k;
    }
}