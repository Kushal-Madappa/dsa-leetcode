"""
LeetCode 525 — Contiguous Array
Difficulty: Medium
Topics: Array, Hash Table, Prefix Sum

Problem
-------
Given a binary array `nums`, return the maximum length of a contiguous
subarray with an equal number of 0s and 1s.

Key insight — transform, then "first-index" map
-----------------------------------------------
Replace every 0 with -1. Now "equal 0s and 1s" becomes "sum == 0".
Walk the array tracking the running sum. The first time we see a given
running sum, record its index. If we see the same running sum later at
index j, then the subarray (first_idx, j] has sum 0  =>  equal 1s and
-1s in the transformed array  =>  equal 0s and 1s in the original.

We want the *longest* such subarray, so we always keep the **earliest
index** for each sum. Seed with `{0: -1}` so a prefix that itself sums
to 0 yields length `j - (-1) = j + 1`.

This is the same skeleton as LC 523, but the key is the raw running
sum (not a remainder), and we track length instead of asking a
yes/no question. Together these two problems define the
"first-index" dialect of prefix-sum + hash map:

    count-map     -> "how many subarrays match?"   (e.g. LC 560, 974)
    first-idx-map -> "exists / longest subarray?"  (e.g. LC 523, 525)

Complexity
----------
Time:   O(n)  — one pass.
Space:  O(n)  — at most n distinct running sums in the worst case.
"""
from __future__ import annotations
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_idx: dict[int, int] = {0: -1}    # sum -> earliest index
        running = 0
        best = 0
        for i, x in enumerate(nums):
            running += 1 if x == 1 else -1
            if running in first_idx:
                best = max(best, i - first_idx[running])
            else:
                first_idx[running] = i
        return best


# ----------------------------- self-tests ---------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1 — [0,1] -> length 2
    assert sol.findMaxLength([0, 1]) == 2

    # Example 2 — [0,1,0] -> [0,1] length 2 (the trailing 0 unbalances)
    assert sol.findMaxLength([0, 1, 0]) == 2

    # All zeros — no balance possible
    assert sol.findMaxLength([0, 0, 0]) == 0
    assert sol.findMaxLength([1, 1, 1]) == 0

    # Balanced across the whole array
    assert sol.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]) == 4  # [1,0,1,1]? actually [0,1,1,0]
    # Verify: [0,1,1,0] indices 0..3 -> two 0s, two 1s -> length 4 ✓

    # Long balanced sequence with a leading unbalanced prefix
    assert sol.findMaxLength([1, 1, 0, 0, 1, 0, 1, 0]) == 8

    # Single element
    assert sol.findMaxLength([0]) == 0
    assert sol.findMaxLength([1]) == 0

    # Empty
    assert sol.findMaxLength([]) == 0

    print("All tests passed for LC 525.")
