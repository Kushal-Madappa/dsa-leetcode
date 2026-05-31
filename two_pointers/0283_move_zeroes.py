# LeetCode: Move Zeroes (#283)
# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Two-pointer: k tracks the next position for a non-zero element.
        Swap-on-find keeps relative order of non-zeros, pushes zeros to the end.
        Time:  O(n)
        Space: O(1)
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
