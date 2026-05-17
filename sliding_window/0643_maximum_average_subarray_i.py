"""
LeetCode #643 — Maximum Average Subarray I
Difficulty  : Easy
Topic tags  : Sliding Window (Fixed Size), Arrays
--------------------------------------------------
Problem
-------
Given an integer array `nums` and an integer `k`, find the contiguous
subarray of length exactly `k` that has the maximum average value and
return that maximum average.

Approach — Fixed-size sliding window
--------------------------------------
1. Compute the sum of the first k elements (the initial window).
2. Slide the window one step at a time: add nums[r], subtract nums[r-k].
3. Track the running maximum sum; return max_sum / k at the end.

Why this works:
  Each slide operation takes O(1) — no need to re-sum k elements.
  We only ever store two numbers (current sum, best sum), so space is O(1).

Complexity
----------
  Time  : O(n)  — one pass after the initial O(k) setup
  Space : O(1)  — only two integer accumulators
"""

from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    """Return the maximum average of any contiguous subarray of length k."""
    # build initial window
    window_sum: int = sum(nums[:k])
    best_sum: int = window_sum

    # slide the window
    for r in range(k, len(nums)):
        window_sum += nums[r] - nums[r - k]   # add right element, drop left
        if window_sum > best_sum:
            best_sum = window_sum

    return best_sum / k


# self-test
if __name__ == "__main__":
    assert findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert findMaxAverage([5], 1) == 5.0
    assert findMaxAverage([0, 4, 0, 3, 2], 1) == 4.0
    assert findMaxAverage([3, 3, 3], 3) == 3.0
    print("All tests passed")
