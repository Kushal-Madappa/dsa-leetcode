# LeetCode: Max Consecutive Ones (#485)
# https://leetcode.com/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = cur = 0
        for x in nums:
            if x == 1:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best
