class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda interval: (interval[1]))
        print(intervals)

        non_overlapping_intervals = []
        removal = 0
        for interval in intervals:
            if(not non_overlapping_intervals):
                non_overlapping_intervals.append(interval)
                continue
        
            last_non_overlapping_interval = non_overlapping_intervals[-1]

            if (interval[0]<last_non_overlapping_interval[1]):
                removal += 1
            else:
                non_overlapping_intervals.append(interval)
            
        return removal

        