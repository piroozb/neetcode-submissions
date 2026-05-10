"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        s = 0
        e = 0
        res = 0
        count = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count += 1
                s += 1
                res = max(count, res)
            else:
                e += 1
                count -= 1
        return res