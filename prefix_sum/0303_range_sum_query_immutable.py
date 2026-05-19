"""
LeetCode #303 — Range Sum Query - Immutable (Easy)
Topics: Array, Prefix Sum, Design

Given an integer array `nums`, handle multiple queries of the form
"return the sum of the elements of `nums` between indices `left` and
`right` inclusive".

The naive approach recomputes the sum on every call: O(n) per query,
O(q * n) total. The prefix-sum design precomputes once and answers in
O(1) per query — a textbook example of trading O(n) build time and
O(n) memory for unbounded query speedups.

Key trick: define P[0] = 0 and P[i] = nums[0] + ... + nums[i-1].
Then sum(nums[l..r]) = P[r+1] - P[l]. The +1 offset is what lets us
include index 0 cleanly with no special case.

Complexity:
  - __init__: O(n) time, O(n) space
  - sumRange: O(1) time, O(1) extra space
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        # P has length n+1; P[0]=0 is the empty-prefix sentinel.
        self.prefix: List[int] = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left: int, right: int) -> int:
        # sum(nums[left..right]) == P[right+1] - P[left]
        return self.prefix[right + 1] - self.prefix[left]


def _run_tests() -> None:
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1     # -2 + 0 + 3
    assert na.sumRange(2, 5) == -1    # 3 + -5 + 2 + -1
    assert na.sumRange(0, 5) == -3    # full range

    single = NumArray([7])
    assert single.sumRange(0, 0) == 7

    zeros = NumArray([0, 0, 0, 0])
    assert zeros.sumRange(1, 3) == 0

    # Many queries on the same instance — O(1) each.
    big = NumArray(list(range(1, 1001)))   # 1..1000
    assert big.sumRange(0, 999) == 1000 * 1001 // 2
    assert big.sumRange(99, 99) == 100
    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
