"""
LeetCode #724 — Find Pivot Index (Easy)
Topics: Array, Prefix Sum

Problem:
    Given an integer array `nums`, return the leftmost pivot index, i.e.
    the index `i` such that the sum of elements strictly to the left of
    `i` equals the sum of elements strictly to the right of `i`.
    If no such index exists return -1.

Pattern (prefix sum):
    Let S = sum(nums) and `left` be the running sum of elements before
    index i. The right sum is then `S - left - nums[i]`. We are looking
    for the first i where `left == S - left - nums[i]`.

    This turns a naive O(n^2) double-scan into a single O(n) pass with
    O(1) extra memory.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


def pivot_index(nums: List[int]) -> int:
    """Return the leftmost pivot index, or -1 if none exists."""
    total: int = sum(nums)
    left: int = 0
    for i, x in enumerate(nums):
        # right sum on the fly — avoids a second prefix array
        if left == total - left - x:
            return i
        left += x
    return -1


if __name__ == "__main__":
    # LeetCode examples
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3, "example 1"
    assert pivot_index([1, 2, 3]) == -1, "example 2"
    assert pivot_index([2, 1, -1]) == 0, "example 3 (left of index 0 is empty)"

    # Edge cases
    assert pivot_index([0]) == 0, "single element — left and right are both empty"
    assert pivot_index([-1, -1, -1, 0, 1, 1]) == 0, "negatives allowed"
    assert pivot_index([1, 2, 3, 4, 6]) == 3, "pivot in the middle (1+2+3 == 6)"
    assert pivot_index([]) == -1, "empty input"

    print("All tests passed.")
