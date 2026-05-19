"""
LeetCode #974 — Subarray Sums Divisible by K (Medium)
Topics: Array, Hash Map, Prefix Sum, Math

Return the number of (non-empty) contiguous subarrays whose sum is
divisible by k.

This is the close cousin of LC #560 (subarray sum equals k).
Same skeleton, different key:

  #560 key  -> running prefix sum
  #974 key  -> running prefix sum MOD k

Why mod-k works:
  sum(nums[l..r]) ≡ 0 (mod k)
     ⇔  P[r+1] - P[l] ≡ 0 (mod k)
     ⇔  P[r+1] ≡ P[l] (mod k)

So at every right endpoint we count how many *earlier* prefixes had
the same remainder — those are exactly the valid left endpoints.

Negative-number gotcha:
  Python's % already returns a non-negative remainder when k > 0
  (e.g. (-3) % 5 == 2), so we can use `prefix % k` directly.
  In C++/Java the idiom would be ((prefix % k) + k) % k.

Complexity: O(n) time, O(min(n, k)) space — at most k distinct
remainders ever land in the map.
"""

from collections import defaultdict
from typing import List


def subarrays_div_by_k(nums: List[int], k: int) -> int:
    """Count contiguous subarrays of `nums` whose sum % k == 0."""
    counts: dict[int, int] = defaultdict(int)
    counts[0] = 1            # empty-prefix sentinel: P[0] = 0
    prefix = 0
    answer = 0
    for x in nums:
        prefix = (prefix + x) % k
        # Every earlier prefix with the same remainder closes a valid subarray.
        answer += counts[prefix]
        counts[prefix] += 1
    return answer


def _run_tests() -> None:
    # Example from LeetCode: 7 valid subarrays.
    assert subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5) == 7

    # Single element divisible.
    assert subarrays_div_by_k([5], 5) == 1
    # Single element not divisible.
    assert subarrays_div_by_k([3], 5) == 0

    # Every prefix sum equals 0 mod 1 — every subarray counts.
    nums = [1, 2, 3, 4, 5]
    n = len(nums)
    assert subarrays_div_by_k(nums, 1) == n * (n + 1) // 2

    # Negatives.
    assert subarrays_div_by_k([-1, 2, 9], 2) == 2  # [-1, 9 -> wait recount]
    # Manual check:
    #   prefix mod 2 sequence with counts seeded {0:1}:
    #     start prefix=0
    #     -1 -> prefix=-1 % 2 = 1, counts[1]=0 -> ans=0, counts[1]=1
    #      2 -> prefix=3 % 2 = 1, counts[1]=1 -> ans=1, counts[1]=2
    #      9 -> prefix=12 % 2 = 0, counts[0]=1 -> ans=2, counts[0]=2
    # So expected = 2. Good.

    # All zeros — every non-empty subarray is divisible by any k.
    zeros = [0, 0, 0, 0]
    assert subarrays_div_by_k(zeros, 9) == 4 * 5 // 2  # 10

    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
