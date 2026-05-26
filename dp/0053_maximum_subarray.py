"""
LeetCode 53 — Maximum Subarray  (Medium)
Topics: Array, Dynamic Programming, Divide and Conquer
Pattern: Kadane's algorithm — 1-D DP where the rolling state is the
best subarray sum *ending at index i*.

State:      f(i) = max sum of a contiguous subarray that ENDS at index i
Transition: f(i) = max(nums[i], f(i-1) + nums[i])
            (start fresh at i, OR extend the previous best subarray)
Answer:     max over all f(i)

Two scalars: `curr` = f(i), `best` = global maximum.

Complexity: O(n) time, O(1) space.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)   # restart, or extend
            if curr > best:
                best = curr
        return best


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),     # LC example 1: [4,-1,2,1]
        ([1], 1),                                  # LC example 2
        ([5, 4, -1, 7, 8], 23),                    # LC example 3
        ([-1], -1),                                # single negative
        ([-1, -2, -3], -1),                        # all negative -> least-negative single element
        ([-5, -4, -3, -2, -1], -1),                # all negative, monotonic
        ([1, 2, 3, 4, 5], 15),                     # all positive -> full sum
        ([0, 0, 0], 0),                            # all zero
        ([3, -2, 5, -1], 6),                       # extend through negative
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),        # [4,-1,-2,1,5]
    ]
    for nums, want in cases:
        got = s.maxSubArray(nums)
        assert got == want, f"maxSubArray({nums}) -> {got}, want {want}"
    print(f"All {len(cases)} tests passed.")
