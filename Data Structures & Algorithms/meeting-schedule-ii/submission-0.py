from _heapq import heappush
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0

        intervals.sort(key = lambda interval: interval.start)
        rooms = []

        for interval in intervals:
            while len(rooms) and interval.start>=rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, interval.end)
            res = max(res, len(rooms))


        return res
        