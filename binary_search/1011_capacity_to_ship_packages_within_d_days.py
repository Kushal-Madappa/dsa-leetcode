"""
LeetCode 1011 — Capacity to Ship Packages Within D Days
Difficulty: Medium
Topics: Array, Binary Search

Problem
-------
You have packages on a conveyor with weights weights[i]. A ship leaves once per
day. We must ship every package in order, in at most `days` days. Each day, we
load packages onto the ship in order until adding the next one would exceed
the ship's capacity. Return the LEAST capacity such that we finish in `days`.

Approach
--------
Parametric binary search on capacity (the answer).
- The capacity must be >= max(weights) (or the heaviest single package can't
  even fit), so lo = max(weights).
- The capacity is never more than sum(weights) (load everything in one day),
  so hi = sum(weights).
- Predicate `can_ship(cap)`: greedy one-pass — start a new day whenever the
  running sum would exceed `cap`; return True iff days_used <= days.
- `can_ship` is monotone in cap (more capacity never needs more days), so
  binary-search the lower-bound of the True region.

Complexity
----------
Time:  O(N * log(sum(weights) - max(weights)))
Space: O(1)
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap: int) -> bool:
            used, load = 1, 0
            for w in weights:
                if load + w > cap:
                    used += 1
                    load = w
                    if used > days:
                        return False
                else:
                    load += w
            return True

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution()

    # LeetCode sample 1
    assert sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15

    # LeetCode sample 2
    assert sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6

    # LeetCode sample 3
    assert sol.shipWithinDays([1, 2, 3, 1, 1], 4) == 3

    # Edge: ship everything in one day -> cap = sum
    assert sol.shipWithinDays([1, 2, 3, 4, 5], 1) == 15

    # Edge: as many days as packages -> cap = max(weights)
    assert sol.shipWithinDays([7, 1, 1, 1, 1], 5) == 7

    # Edge: single package
    assert sol.shipWithinDays([42], 1) == 42

    # Edge: all equal weights
    assert sol.shipWithinDays([5, 5, 5, 5], 2) == 10

    # Brute-force cross-check on a few random small inputs
    import random
    def brute(weights, days):
        for cap in range(max(weights), sum(weights) + 1):
            used, load = 1, 0
            for w in weights:
                if load + w > cap:
                    used += 1
                    load = w
                else:
                    load += w
            if used <= days:
                return cap
        return sum(weights)

    random.seed(0)
    for _ in range(200):
        n = random.randint(1, 12)
        ws = [random.randint(1, 9) for _ in range(n)]
        d = random.randint(1, n)
        assert sol.shipWithinDays(ws, d) == brute(ws, d), (ws, d)

    print("All tests passed.")
