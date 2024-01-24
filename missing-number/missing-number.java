class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> seen = new HashSet<>(Arrays.asList(Arrays.stream(nums).boxed().toArray(Integer[]::new)));
        
        for(int i = 0; i < nums.length; i++){
            if(!seen.contains(i)){
                return i;
            }
        }
        
        return nums.length;
    }
}