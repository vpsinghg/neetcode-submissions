class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0
        merged = []
        n =  len(intervals)
        if n == 0:
            return [newInterval]


        while i < n:
            if(intervals[i][1]<newInterval[0]):
                merged.append(intervals[i])
                i += 1
            else:
                break

        merged.append(newInterval)
        
        # append and handle overlapping with the ramainig intervals

        while(i < n):
            if(merged[-1][1] < intervals[i][0]):
                merged.append(intervals[i])
            else:
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            i += 1
        
        return merged

        