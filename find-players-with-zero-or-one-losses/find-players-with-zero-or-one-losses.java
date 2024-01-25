class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Set<Integer> players = new HashSet<>();
        Map<Integer, Integer> lossCount = new HashMap<>();
        List<List<Integer>> result = new ArrayList<>();
        
        for(int[] match : matches){
            int winner = match[0];
            int loser = match[1];
            players.add(winner);
            players.add(loser);
            
            lossCount.put(loser, lossCount.getOrDefault(loser, 0) + 1);
        }
        
        List<Integer> oneLoss = new ArrayList<>();
        List<Integer> noLoss = new ArrayList<>();
        for(int player : players){
            if(!lossCount.containsKey(player)){
                noLoss.add(player);
            }else if(lossCount.get(player) == 1){
                oneLoss.add(player);
            }
        }
        
        Collections.sort(noLoss);
        Collections.sort(oneLoss);
        
        result.add(noLoss);
        result.add(oneLoss);
        return result;
    }
}