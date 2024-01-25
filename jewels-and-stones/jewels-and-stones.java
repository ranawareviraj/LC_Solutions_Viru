class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jewelSet = new HashSet<>();
        int count = 0;
        
        for(char jewel : jewels.toCharArray()){
            jewelSet.add(jewel);
        }
        
        for(char stone : stones.toCharArray()){
            if(jewelSet.contains(stone)){
                count += 1;
            }
        }
        
        return count;
    }
}