# LeetCode: Jump Game (#55)
# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            if i + jump > max_reach:
                max_reach = i + jump
        return True
