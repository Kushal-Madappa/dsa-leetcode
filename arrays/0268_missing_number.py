# LeetCode: Missing Number (#268)
# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
