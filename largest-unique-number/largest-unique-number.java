class Solution {
    public int largestUniqueNumber(int[] nums) {
        int largest = Integer.MIN_VALUE;
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        for(int key: map.keySet()){
            int freq = map.get(key);
            if(freq == 1){
                largest = Math.max(largest, key);
            }
        }
        
        return largest == Integer.MIN_VALUE ? -1 : largest;
    }
}