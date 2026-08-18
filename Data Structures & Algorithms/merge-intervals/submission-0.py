class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged = []
        intervals.sort(key=lambda interval: interval[0])

        for interval in intervals:
            if not merged:
                merged.append(interval)
                continue
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])

            else:
                merged.append(interval)

        return merged
