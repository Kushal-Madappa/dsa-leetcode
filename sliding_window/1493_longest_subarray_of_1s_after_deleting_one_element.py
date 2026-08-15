# LeetCode: Longest Subarray of 1's After Deleting One Element (#1493)
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        best = 0
        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            # window length minus the single deletion we're allowed
            best = max(best, right - left)
        return best
