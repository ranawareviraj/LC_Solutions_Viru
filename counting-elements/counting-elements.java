class Solution {
    public int countElements(int[] arr) {
        int count = 0;
        Map<Integer, Integer> numToCount = new HashMap<>();
        for(int num : arr){
            numToCount.put(num, numToCount.getOrDefault(num, 0) + 1);
        }
        
        for(int key : numToCount.keySet()){
            if(numToCount.containsKey(key + 1)){
                count += numToCount.get(key);
            }
        }
        
        return count;
    }
}