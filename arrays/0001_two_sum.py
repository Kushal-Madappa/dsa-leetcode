"""
LeetCode 1: Two Sum
Difficulty: Easy
Topics: Array, Hash Table

Problem
-------
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`. Each input has exactly
one solution, and you may not use the same element twice.

Example
-------
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Because nums[0] + nums[1] == 2 + 7 == 9.

Approach
--------
1. Brute force (O(n^2)):
   Check every pair (i, j). Too slow for large n.

2. Hash map, single pass (O(n)) -- the canonical pattern:
   As we walk through nums, store each value's index in a dict.
   For each `num`, the value we need to pair with is `complement = target - num`.
   If `complement` is already in the dict, we found our answer.

Complexity
----------
    Time:  O(n)  -- one pass, O(1) average hash lookups.
    Space: O(n)  -- the dict may store up to n entries.

Why this matters
----------------
"Use a hash map for O(1) lookup" is one of the most common interview patterns.
This problem is the cleanest place to internalize it.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # the problem guarantees a solution; defensive return


if __name__ == "__main__":
    sol = Solution()

    # Basic example from the problem statement
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    # Answer is not at the front of the list
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    # Duplicates that form the answer
    assert sol.twoSum([3, 3], 6) == [0, 1]
    # Negative numbers
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

    print("All tests passed.")
