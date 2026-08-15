# LeetCode: Shuffle the Array (#1470)
# https://leetcode.com/problems/shuffle-the-array/
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result
