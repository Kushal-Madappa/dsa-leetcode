# LeetCode: Contains Duplicate II (#219)
# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for i, v in enumerate(nums):
            if v in last_index and i - last_index[v] <= k:
                return True
            last_index[v] = i
        return False
