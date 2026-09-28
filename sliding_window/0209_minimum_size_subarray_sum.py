# LeetCode: Minimum Size Subarray Sum (#209)
# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        cur = 0
        best = n + 1
        for right in range(n):
            cur += nums[right]
            while cur >= target:
                best = min(best, right - left + 1)
                cur -= nums[left]
                left += 1
        return 0 if best == n + 1 else best
