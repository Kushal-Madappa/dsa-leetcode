# LeetCode: Minimum Number of Arrows to Burst Balloons (#452)
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for s, e in points[1:]:
            if s > end:
                arrows += 1
                end = e
        return arrows
