"""
LeetCode 704 — Binary Search (Easy)
====================================

Topic: Binary Search (canonical template)
URL:   https://leetcode.com/problems/binary-search/

Problem
-------
Given a sorted (ascending) array `nums` of distinct integers and a
target value `target`, return the index of `target` if it exists in
`nums`, otherwise return -1. Solution must run in O(log n) time.

Approach
--------
The canonical "closed interval" binary-search template.

    Invariant: if `target` exists in `nums`, its index is inside
               the closed interval [lo, hi].

We maintain that invariant by shrinking the interval one side at a
time:
    - If `nums[mid] == target`, we're done.
    - If `nums[mid] <  target`, the answer (if any) is to the right
      of `mid`, so the new interval is [mid + 1, hi].
    - If `nums[mid] >  target`, the answer (if any) is to the left
      of `mid`, so the new interval is [lo, mid - 1].

We loop while `lo <= hi`. The interval is non-empty exactly when
`lo <= hi`; once `lo > hi`, the interval is empty and the answer
isn't in the array, so we return -1.

Why `mid = lo + (hi - lo) // 2` and not `(lo + hi) // 2`?
In Python it doesn't matter (ints are arbitrary precision), but in
C/Java/C++ the second form can overflow for large `lo + hi`. We
write the safe form here so the same template ports verbatim to
other languages.

Complexity
----------
Time:  O(log n)  -- the search interval halves every iteration.
Space: O(1)      -- a constant number of pointers.

Common pitfalls
---------------
- Using `lo < hi` with the [lo, hi] convention skips a single-element
  check (the case `lo == hi`). Match the loop condition to your
  interval convention: closed `[lo, hi]` -> `while lo <= hi`,
  half-open `[lo, hi)` -> `while lo < hi`. Pick one and stick to it.
- Forgetting the `+ 1` / `- 1` updates on `lo` / `hi` after probing
  `mid` is the source of the classic "infinite loop" binary-search
  bug.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """Return the index of `target` in sorted `nums`, or -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    # LeetCode official examples
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Edge cases
    assert search([], 5) == -1                # empty array
    assert search([5], 5) == 0                # single element, hit
    assert search([5], 3) == -1               # single element, miss
    assert search([1, 2, 3, 4, 5], 1) == 0    # leftmost
    assert search([1, 2, 3, 4, 5], 5) == 4    # rightmost
    assert search([-5, -3, -1, 0, 2], -3) == 1  # negatives

    # Larger array -- checks log behaviour doesn't break correctness
    big = list(range(0, 10_000, 2))           # even numbers
    assert search(big, 4242) == 2121
    assert search(big, 4243) == -1            # odd number, not present

    print("All tests passed.")
