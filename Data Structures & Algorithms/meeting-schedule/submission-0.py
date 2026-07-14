"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        end = None
        intervals.sort(key = lambda x : x.start)
        for i in intervals:
            if not end:
                end = i.end
            else:
                if i.start < end:
                    return False
                end = i.end
        return True