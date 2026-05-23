"""
LeetCode 875 — Koko Eating Bananas (Medium)
https://leetcode.com/problems/koko-eating-bananas/

Topic: Binary Search on the Answer (parametric search).

Approach
--------
We want the smallest integer eating-rate `k` (bananas/hour) such that
Koko can finish every pile within `h` hours. For a fixed `k`, the hours
needed to clear pile `p` are `ceil(p / k) = (p + k - 1) // k` because
Koko cannot move on from a pile within the same hour she finishes it.
Sum that over all piles to get `hours(k)`.

Two key observations make this a binary search:
  1. The answer must lie in `[1, max(piles)]` — any `k > max(piles)` is
     dominated by `k = max(piles)` (you still spend 1 hour per pile).
  2. `hours(k)` is monotonically non-increasing in `k`. So the predicate
     `hours(k) <= h` flips from False to True exactly once across the
     answer space. We want the *leftmost* True, i.e. `lower_bound` of
     the predicate over `[1, max(piles)]` — the half-open template
     from Day 9.

Complexity
----------
Let n = len(piles), M = max(piles).
  Time:  O(n * log M) — log M binary-search steps, each O(n) to score.
  Space: O(1).
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k: int) -> int:
            # ceil(p / k) without floats, summed across all piles.
            return sum((p + k - 1) // k for p in piles)

        lo, hi = 1, max(piles)  # half-open [lo, hi]
        while lo < hi:
            mid = (lo + hi) // 2
            if hours(mid) <= h:
                hi = mid          # mid is feasible — pull the ceiling down
            else:
                lo = mid + 1      # mid too slow — discard everything <= mid
        return lo


if __name__ == "__main__":
    s = Solution()

    # LeetCode sample 1
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4

    # LeetCode sample 2
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

    # LeetCode sample 3
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    # Edge: single pile, h equals pile size -> rate 1 suffices.
    assert s.minEatingSpeed([1], 1) == 1

    # Edge: single pile, lots of time -> still need at least rate 1.
    assert s.minEatingSpeed([7], 100) == 1

    # Edge: single huge pile, tight schedule -> ceil(p / h).
    assert s.minEatingSpeed([1_000_000_000], 2) == 500_000_000

    # Edge: h equals n -> rate must be max(piles) (one hour per pile).
    assert s.minEatingSpeed([5, 4, 3, 2, 1], 5) == 5

    # Brute-force cross-check on small inputs.
    import random
    random.seed(0)
    def brute(piles, h):
        for k in range(1, max(piles) + 1):
            if sum((p + k - 1) // k for p in piles) <= h:
                return k
        return -1
    for _ in range(200):
        n = random.randint(1, 6)
        piles = [random.randint(1, 20) for _ in range(n)]
        h = random.randint(n, 4 * n + 5)
        assert s.minEatingSpeed(piles, h) == brute(piles, h), (piles, h)

    print("All tests passed.")
