class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = [stick for stick in sticks]
        heapq.heapify(heap)
        cost = 0
        
        while len(heap) > 1:
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)
            new_stick = stick1 + stick2
            cost += new_stick 
            heapq.heappush(heap, new_stick)
        
        return cost