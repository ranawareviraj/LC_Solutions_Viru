class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles ]
        heapq.heapify(heap)
        
        for i in range(k):
            pile = -heapq.heappop(heap)
            heapq.heappush(heap, -(pile - pile // 2))
        
        remaining_stones = 0
        while heap:
            pile = -heapq.heappop(heap)
            remaining_stones += pile
        
        return remaining_stones