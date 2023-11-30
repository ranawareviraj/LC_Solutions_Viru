class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        merged_intervals = []
        
        for i in range(n):
            # newInterval is ending before current interval
            if newInterval[1] < intervals[i][0]:
                merged_intervals.append(newInterval)
                merged_intervals.extend(intervals[i:])
                return merged_intervals
            # newInterval is starting after current interval ends
            elif newInterval[0] > intervals[i][1]:
                merged_intervals.append(intervals[i])
            # newInterval is overlapping with the current interval
            else:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end]

        # If we reach this far, means we havent inserted newInterval (or merged newInterval)
        merged_intervals.append(newInterval)
        
        # return all merged_intervals
        return merged_intervals
