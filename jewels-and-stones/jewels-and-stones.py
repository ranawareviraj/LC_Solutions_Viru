class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_counter = Counter(stones)
        count = 0
        
        for jewel in jewels:
            if jewel in stones_counter:
                count += stones_counter[jewel]
        
        return count
            