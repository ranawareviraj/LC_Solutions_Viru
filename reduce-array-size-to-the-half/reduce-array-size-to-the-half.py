class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, -num))
        
        curr = 0
        count = 0
        while heap and curr < len(arr) / 2:
            curr_freq = -heapq.heappop(heap)[0]
            curr += curr_freq
            count += 1
        
        return count
            