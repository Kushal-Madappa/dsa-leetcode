# LeetCode: Max Consecutive Ones III (#1004)
# https://leetcode.com/problems/max-consecutive-ones-iii/
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0
        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if right - left + 1 > best:
                best = right - left + 1
        return best
