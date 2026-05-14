"""
LeetCode 217: Contains Duplicate
Difficulty: Easy
Topics: Array, Hash Table, Sorting

Problem
-------
Given an integer array `nums`, return True if any value appears at least twice
in the array, and False if every element is distinct.

Example
-------
    Input:  nums = [1, 2, 3, 1]
    Output: True

    Input:  nums = [1, 2, 3, 4]
    Output: False

Approach
--------
1. Brute force (O(n^2)):
   Compare every pair. Too slow at scale.

2. Sort + adjacent scan (O(n log n)):
   After sorting, duplicates sit side by side. Cheap on memory but pays a
   log factor.

3. Hash set, single pass (O(n)) -- the canonical pattern:
   Walk the array, asking the set "have I seen this before?" If yes, done.
   Otherwise insert. The set replaces a nested search with a constant-time
   probe.

   The slickest form is even shorter: `len(set(nums)) != len(nums)`. Same
   complexity, but the explicit loop short-circuits on the first duplicate,
   which can be much faster on lists that have early collisions.

Complexity
----------
    Time:  O(n)  -- one pass with O(1) average set operations.
    Space: O(n)  -- the set may hold up to n distinct values.

Why this matters
----------------
This is the "membership check" sibling of Two Sum's index lookup. Whenever
you need to know "have I seen this thing already?" reach for a set.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()

    # Has a duplicate
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    # All unique
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    # Many duplicates
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    # Single element
    assert sol.containsDuplicate([7]) is False
    # Empty array
    assert sol.containsDuplicate([]) is False
    # Negative numbers and zero
    assert sol.containsDuplicate([-1, 0, 1, -1]) is True

    print("All tests passed.")
