# LeetCode: Summary Ranges (#228)
# https://leetcode.com/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if nums[i] == start:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            i += 1
        return result
