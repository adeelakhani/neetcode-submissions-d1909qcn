"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        start.sort()
        end = [i.end for i in intervals]
        end.sort()
        s, e = 0, 0
        count, maxCount = 0, 0
        while e < len(end):
            if s < len(start) and start[s] < end[e]:
                count+=1
                s+=1
            else:
                count -=1
                e+=1
            if count > maxCount:
                maxCount = count
        return maxCount