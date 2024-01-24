class Solution {
    public int[] getAverages(int[] nums, int k) {
        if (k == 0) {
            return nums;
        }

        int n = nums.length;
        // Fill averages array with default values -1
        int[] averages = new int[n];
        Arrays.fill(averages, -1);

        // Build Prefix Sum - another way
        long[] prefixSum = new long[n + 1];
        for(int i = 0; i < n; i++){
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        // For valid records, update average
        for(int i = k; i < (n - k); i++){
            long sum = prefixSum[i + k + 1] - prefixSum[i - k];
            averages[i] = (int) (sum / (2 * k + 1));
        }

        return averages;
    }
}