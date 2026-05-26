"""
LeetCode 198 — House Robber  (Medium)
Topics: Dynamic Programming, Array
Pattern: 1-D DP with a take/skip decision per index.

State:      f(i) = max amount robbable from houses nums[0..i]
Transition: f(i) = max(f(i-1),               # skip house i
                       f(i-2) + nums[i])     # rob house i (must skip i-1)
Base:       f(-1) = 0, f(0) = nums[0]

Two-variable rolling window keeps space at O(1).

Complexity: O(n) time, O(1) space.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0  # f(i-2), f(i-1)
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2, prev1 = prev1, curr
        return prev1


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([1, 2, 3, 1], 4),                       # LC example 1: rob 1 + 3 = 4
        ([2, 7, 9, 3, 1], 12),                   # LC example 2: rob 2 + 9 + 1 = 12
        ([2, 1, 1, 2], 4),                       # rob 2 + 2 (skip middle pair) = 4
        ([5], 5),                                # single house
        ([5, 1], 5),                             # two houses, rob bigger
        ([1, 5], 5),                             # two houses, rob bigger (other side)
        ([0, 0, 0, 0], 0),                       # all zero
        ([100, 1, 1, 100], 200),                 # rob ends
        ([2, 1, 1, 2, 7], 10),                   # rob 2 + 1 + 7 = 10
        ([6, 6, 4, 8, 4, 3, 3, 10], 27),         # 6 + 8 + 3 + 10 = 27
    ]
    for nums, want in cases:
        got = s.rob(nums)
        assert got == want, f"rob({nums}) -> {got}, want {want}"
    print(f"All {len(cases)} tests passed.")
