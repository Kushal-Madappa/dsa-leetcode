# LeetCode: Remove Duplicates from Sorted Array II (#80)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or nums[k - 2] != x:
                nums[k] = x
                k += 1
        return k
