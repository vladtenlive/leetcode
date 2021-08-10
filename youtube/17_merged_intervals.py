"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda x: x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False

        return True