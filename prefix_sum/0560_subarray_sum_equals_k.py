"""
LeetCode #560 — Subarray Sum Equals K (Medium)
Topics: Array, Hash Table, Prefix Sum

Problem:
    Given an integer array `nums` and an integer `k`, return the total
    number of *contiguous* subarrays whose sum equals `k`.
    `nums` may contain negative values, so a sliding window does NOT
    work — the prefix-sum + hash-map trick does.

Key idea (prefix sum + hash map):
    Let P[i] = nums[0] + nums[1] + ... + nums[i-1] (P[0] = 0).
    The sum of subarray nums[l..r-1] = P[r] - P[l].
    We want to count pairs (l, r) with l < r and P[r] - P[l] == k,
    i.e. P[l] == P[r] - k.

    Walk r left-to-right, keep a hash map { prefix_value: count_of_l }.
    At each step add `counts.get(P[r] - k, 0)` to the answer, then
    register P[r] in the map.

    Pre-seeding the map with {0: 1} accounts for subarrays that start
    at index 0 (i.e. when P[r] itself equals k).

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    """Count contiguous subarrays of `nums` that sum to `k`."""
    counts: "defaultdict[int, int]" = defaultdict(int)
    counts[0] = 1  # empty-prefix sentinel — enables subarrays starting at 0

    prefix: int = 0
    answer: int = 0
    for x in nums:
        prefix += x
        # number of earlier prefixes that, when subtracted, leave exactly k
        answer += counts[prefix - k]
        counts[prefix] += 1
    return answer


if __name__ == "__main__":
    # LeetCode examples
    assert subarray_sum([1, 1, 1], 2) == 2, "example 1"
    assert subarray_sum([1, 2, 3], 3) == 2, "example 2 ([1,2] and [3])"

    # Negatives — the reason sliding window fails here
    assert subarray_sum([1, -1, 0], 0) == 3, "[-1,0], [0], [1,-1,0]... wait recount"
    # Manual recount for the above:
    #   [1,-1] sum=0    ✓
    #   [-1,0,...] sums: [-1,0]=−1; [0]=0    ✓ (one occurrence of [0])
    #   [1,-1,0]=0      ✓
    # → exactly 3.

    # All-zero array — every non-empty subarray sums to 0
    # n=4 → C(4+1, 2) = 10 non-empty contiguous subarrays
    assert subarray_sum([0, 0, 0, 0], 0) == 10, "n*(n+1)/2 subarrays sum to 0"

    # Large negative k
    assert subarray_sum([-1, -1, 1], 0) == 1, "subarray [-1, 1]"

    # No matches
    assert subarray_sum([1, 2, 3], 7) == 0, "no subarray sums to 7"

    # Single element matching k
    assert subarray_sum([5], 5) == 1, "single-element match"
    assert subarray_sum([5], 4) == 0, "single-element no match"

    print("All tests passed.")
