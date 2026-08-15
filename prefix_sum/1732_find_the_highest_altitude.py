# LeetCode: Find the Highest Altitude (#1732)
# https://leetcode.com/problems/find-the-highest-altitude/
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for g in gain:
            altitude += g
            if altitude > highest:
                highest = altitude
        return highest
