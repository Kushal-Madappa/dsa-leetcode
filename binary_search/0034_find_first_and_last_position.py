"""
LeetCode 34 -- Find First and Last Position of Element in Sorted Array (Medium)
==============================================================================

Topic: Binary Search (lower_bound + upper_bound)
URL:   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Problem
-------
Given a sorted array of integers `nums` (with possible duplicates)
and a `target`, return `[first, last]` -- the first and last index
where `target` appears -- or `[-1, -1]` if it is not present. Must
run in O(log n).

Approach
--------
Two binary searches, both half-open:

    lower_bound(target):
        leftmost i with nums[i] >= target.
        Predicate: p(mid) = (nums[mid] >= target)
        Update:    hi = mid (keep), lo = mid + 1 (discard).

    upper_bound(target):
        leftmost i with nums[i] >  target.
        Predicate: p(mid) = (nums[mid] >  target)
        Update:    hi = mid (keep), lo = mid + 1 (discard).

If `lo = lower_bound(target)` is past the array OR `nums[lo] != target`,
the target is absent -- return `[-1, -1]`. Otherwise:

    first = lower_bound(target)
    last  = upper_bound(target) - 1

This pair `(lower_bound, upper_bound)` shows up constantly: number
of equal elements is `upper_bound(t) - lower_bound(t)`, range insertion
points are `[lower_bound(t), upper_bound(t)]`, etc.

Complexity
----------
Time:  O(log n) -- two binary searches
Space: O(1)

Edge cases
----------
- Empty array -> [-1, -1].
- Target smaller than all / larger than all elements -> [-1, -1].
- Target equals every element -> [0, n - 1].
- Single occurrence -> first == last.
"""

from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    """Leftmost index i with nums[i] >= target, or len(nums) if none."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    """Leftmost index i with nums[i] > target, or len(nums) if none."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_range(nums: List[int], target: int) -> List[int]:
    """Return [first, last] indices of target in sorted nums, or [-1, -1]."""
    left = lower_bound(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = upper_bound(nums, target) - 1
    return [left, right]


if __name__ == "__main__":
    # LeetCode official examples
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]

    # Edge cases
    assert search_range([1], 1) == [0, 0]                 # single match
    assert search_range([1], 2) == [-1, -1]               # single miss
    assert search_range([2, 2, 2, 2], 2) == [0, 3]        # all matches
    assert search_range([1, 2, 3, 4, 5], 0) == [-1, -1]   # below range
    assert search_range([1, 2, 3, 4, 5], 6) == [-1, -1]   # above range
    assert search_range([1, 2, 3, 4, 5], 1) == [0, 0]     # first index
    assert search_range([1, 2, 3, 4, 5], 5) == [4, 4]     # last index
    assert search_range([1, 1, 2, 3, 3, 3, 5], 3) == [3, 5]

    # Cross-check with bisect: lower_bound == bisect_left,
    # upper_bound == bisect_right.
    import bisect
    arr = [1, 2, 2, 3, 5, 5, 5, 7, 9]
    for t in range(0, 11):
        assert lower_bound(arr, t) == bisect.bisect_left(arr, t), t
        assert upper_bound(arr, t) == bisect.bisect_right(arr, t), t

    print("All tests passed.")
