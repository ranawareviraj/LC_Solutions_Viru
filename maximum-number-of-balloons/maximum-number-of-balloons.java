class Solution {
    public int maxNumberOfBalloons(String text) {
        String pattern = "balloon";
        Map<Character, Integer> patternMap = new HashMap<>();
        Map<Character, Integer> map = new HashMap<>();
        for(char ch: pattern.toCharArray()){
            patternMap.put(ch, patternMap.getOrDefault(ch, 0) + 1);
        }
        
        for(char ch: text.toCharArray()){
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        
        int minFreq = Integer.MAX_VALUE;
        for(char key: patternMap.keySet()){
            int patternFreq = patternMap.get(key);
            int freq = map.getOrDefault(key, 0);
            
            minFreq = Math.min(minFreq, freq / patternFreq);
        }
        
        return minFreq;
    }
}