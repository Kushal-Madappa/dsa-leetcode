# LeetCode: Find All Numbers Disappeared in an Array (#448)
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # In-place marking: negate value at index (num-1) to mark that num was seen.
        # Any index still holding a positive value corresponds to a missing number.
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i + 1 for i, v in enumerate(nums) if v > 0]
