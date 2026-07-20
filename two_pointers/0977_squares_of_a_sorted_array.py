# LeetCode: Squares of a Sorted Array (#977)
# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            lsq, rsq = nums[left] * nums[left], nums[right] * nums[right]
            if lsq > rsq:
                res[pos] = lsq
                left += 1
            else:
                res[pos] = rsq
                right -= 1
            pos -= 1
        return res
