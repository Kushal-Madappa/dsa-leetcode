# LeetCode: Rotate Array (#189)
# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return
        # Reverse whole array, then reverse first k, then reverse rest.
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
