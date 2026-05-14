"""LeetCode 167 — Two Sum II: Input Array Is Sorted (Medium).

Given a 1-indexed sorted array `numbers`, return the 1-indexed positions
of the two values that add up to `target`. Exactly one solution exists.

Pattern: opposite-ends two pointers. Because the array is sorted, the
sum's response to a pointer move is deterministic:
  - sum too small  -> move left forward (need a larger left value)
  - sum too big    -> move right backward (need a smaller right value)
This is the simplest place where sortedness lets us drop a dict.

Time:  O(n) — each pointer moves at most n steps in total.
Space: O(1).
"""

from __future__ import annotations
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]  # problem uses 1-indexing
            if s < target:
                left += 1
            else:
                right -= 1
        return []  # unreachable per problem guarantees


def _test() -> None:
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    assert sol.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    print("0167_two_sum_ii: all tests passed.")


if __name__ == "__main__":
    _test()
