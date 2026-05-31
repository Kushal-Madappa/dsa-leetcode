# LeetCode: Minimum Difference Between Highest and Lowest of K Scores (#1984)
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        best = float('inf')
        for i in range(len(nums) - k + 1):
            best = min(best, nums[i + k - 1] - nums[i])
        return best
