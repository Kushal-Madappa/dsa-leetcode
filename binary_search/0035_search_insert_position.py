"""
LeetCode 35 — Search Insert Position (Easy)
============================================

Topic: Binary Search (lower_bound / leftmost-true template)
URL:   https://leetcode.com/problems/search-insert-position/

Problem
-------
Given a sorted array of distinct integers `nums` and a `target`,
return the index where `target` is found. If not found, return the
index where it would be inserted in order. Must run in O(log n).

Approach
--------
This is the canonical *lower_bound* problem: find the leftmost index
`i` such that `nums[i] >= target`. That index is either:
    - where `target` already sits (found), or
    - where it should be inserted to keep the array sorted.

We use the **half-open** binary-search template here for variety
(0704_binary_search.py uses the closed-interval template; together
they cover the two patterns you'll reuse forever):

    Invariant: the answer lies in the half-open interval [lo, hi).
               After the loop, lo == hi == answer.

Inside the loop:
    - If `nums[mid] >= target`, `mid` is a *candidate* answer, so
      we keep it in our window: hi = mid (NOT mid - 1).
    - If `nums[mid] <  target`, `mid` cannot be the answer, so we
      discard it: lo = mid + 1.

We loop while `lo < hi`. When `lo == hi`, the window is a single
slot and that slot is the answer.

Why this template?
------------------
The "leftmost index satisfying a predicate" pattern shows up
everywhere -- first bad version (LC #278), search range (LC #34),
search in rotated array (LC #33), find peak (LC #162). Once the
predicate is `p(mid) = (nums[mid] >= target)`, every problem in the
family is a one-line change.

Complexity
----------
Time:  O(log n)
Space: O(1)

Edge cases / pitfalls
---------------------
- `target` smaller than all elements -> insertion at index 0.
- `target` larger than all elements  -> insertion at index n.
  This is why we initialise `hi = len(nums)` (NOT `len(nums) - 1`):
  the answer is allowed to be one past the last index.
- An empty array returns 0 (insert at the start).
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """Return leftmost index i with nums[i] >= target, else len(nums)."""
    lo, hi = 0, len(nums)         # half-open [lo, hi); hi may equal len
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid              # keep mid in the candidate window
        else:
            lo = mid + 1          # discard mid
    return lo


if __name__ == "__main__":
    # LeetCode official examples
    assert search_insert([1, 3, 5, 6], 5) == 2      # found
    assert search_insert([1, 3, 5, 6], 2) == 1      # inserted between
    assert search_insert([1, 3, 5, 6], 7) == 4      # inserted at end

    # Edge cases
    assert search_insert([], 5) == 0                # empty
    assert search_insert([1], 0) == 0               # insert before single
    assert search_insert([1], 2) == 1               # insert after single
    assert search_insert([1, 3, 5, 6], 0) == 0      # smaller than all
    assert search_insert([1, 3, 5, 6], 1) == 0      # leftmost match
    assert search_insert([1, 3, 5, 6], 6) == 3      # rightmost match
    assert search_insert([-5, -3, 0, 4], -4) == 1   # negatives

    # Consistency with built-in bisect.bisect_left -- nice sanity check
    import bisect
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    for t in range(0, 17):
        assert search_insert(arr, t) == bisect.bisect_left(arr, t), t

    print("All tests passed.")
