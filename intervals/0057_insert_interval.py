# LeetCode: Insert Interval (#57)
# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        i, n = 0, len(intervals)
        # add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        # add the rest
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
