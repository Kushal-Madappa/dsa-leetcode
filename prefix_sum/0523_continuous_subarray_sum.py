"""
LeetCode 523 — Continuous Subarray Sum
Difficulty: Medium
Topics: Array, Hash Table, Math, Prefix Sum

Problem
-------
Given an integer array `nums` and an integer `k`, return True iff `nums`
has a contiguous subarray of length >= 2 whose sum is a multiple of `k`
(0 counts as a multiple of every k).

Key insight — "first-index" dialect of prefix-sum + hash map
------------------------------------------------------------
Let P[i] = nums[0] + nums[1] + ... + nums[i-1]   (P[0] = 0).

    sum(nums[l..r-1]) % k == 0
        <=>  (P[r] - P[l]) % k == 0
        <=>  P[r] % k == P[l] % k

So we walk left->right tracking `prefix % k`. The first time we see a
remainder we **record the index** (not a count). The next time we see
the same remainder at index `j`, the subarray (i, j] has length `j - i`
and sum divisible by k. We only return True when `j - i >= 2`, so the
"first-index" map is exactly what we need — a count map can't answer
"length >= 2".

Seed the map with `{0: -1}` so that a prefix that itself is divisible
by k (e.g. nums = [0,0]) still works: P[r] % k == 0 matches the
sentinel at index -1, length = r - (-1) >= 2 when r >= 1.

Complexity
----------
Time:   O(n)        — one pass.
Space:  O(min(n,k)) — at most k distinct remainders.
"""
from __future__ import annotations
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Map: remainder -> earliest index where it appeared
        first_idx: dict[int, int] = {0: -1}
        prefix = 0
        for i, x in enumerate(nums):
            prefix = (prefix + x) % k          # Python's % is always non-negative for k > 0
            if prefix in first_idx:
                if i - first_idx[prefix] >= 2:
                    return True
                # Don't overwrite — we want the earliest index so future
                # matches yield the longest possible subarray.
            else:
                first_idx[prefix] = i
        return False


# ----------------------------- self-tests ---------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1 — [23,2,4,6,7], k=6  -> [2,4] sums to 6  -> True
    assert sol.checkSubarraySum([23, 2, 4, 6, 7], 6) is True

    # Example 2 — [23,2,6,4,7], k=6  -> [23,2,6,4,7] sums to 42 = 7*6 -> True
    assert sol.checkSubarraySum([23, 2, 6, 4, 7], 6) is True

    # Example 3 — [23,2,6,4,7], k=13 -> no subarray works -> False
    assert sol.checkSubarraySum([23, 2, 6, 4, 7], 13) is False

    # Edge — length-1 input can never satisfy length >= 2
    assert sol.checkSubarraySum([5], 5) is False

    # Edge — two zeros are a length-2 subarray summing to 0, which is 0*k
    assert sol.checkSubarraySum([0, 0], 1) is True

    # Edge — single zero with another non-multiple still has [0,0]? No, only one 0.
    assert sol.checkSubarraySum([1, 0], 2) is False

    # Edge — large k where only the trivial prefix matches the seed
    assert sol.checkSubarraySum([1, 2, 3], 100) is False

    # Edge — exact multiple at the very start, length 2
    assert sol.checkSubarraySum([6, 1], 6) is False  # [6] is len 1, [6,1]=7 not multiple
    assert sol.checkSubarraySum([6, 0], 6) is True   # [6,0] = 6 = 1*6, length 2

    print("All tests passed for LC 523.")
