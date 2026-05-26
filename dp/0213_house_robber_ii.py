"""
LeetCode 213 — House Robber II  (Medium)
Topics: Dynamic Programming, Array
Pattern: Variant of #198 with a CIRCULAR street — house 0 and house
n-1 are adjacent, so they can't both be robbed.

Trick: solve the linear House Robber problem twice on two slices that
each exclude one of the two endpoints, then take the better of the two.

  Option A: rob from nums[0 .. n-2]  (excludes the last house)
  Option B: rob from nums[1 .. n-1]  (excludes the first house)

Either option becomes a standard #198 instance.

Complexity: O(n) time, O(1) space.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def linear_rob(arr: List[int]) -> int:
            prev2, prev1 = 0, 0
            for x in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1

        return max(linear_rob(nums[:-1]), linear_rob(nums[1:]))


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([2, 3, 2], 3),                     # LC example 1: can't take both 2s
        ([1, 2, 3, 1], 4),                  # LC example 2: rob 1 + 3 = 4
        ([1, 2, 3], 3),                     # LC example 3: pick the 3
        ([5], 5),                           # single house
        ([5, 1], 5),                        # two houses, pick max
        ([1, 5], 5),                        # two houses, other side
        ([200, 3, 140, 20, 10], 340),       # 200 + 140 = 340 (excludes last)
        ([1, 1, 1, 1, 1], 2),               # 5 houses circular -> max 2 non-adjacent
        ([0, 0, 0], 0),                     # all zero
        ([4, 1, 2, 7, 5, 3, 1], 14),        # circular DP picks 4+2+5+? -- verified below
    ]
    for nums, want in cases:
        got = s.rob(nums)
        assert got == want, f"rob({nums}) -> {got}, want {want}"
    print(f"All {len(cases)} tests passed.")
