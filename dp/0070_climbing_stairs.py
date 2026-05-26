"""
LeetCode #70 — Climbing Stairs (Easy)
Topics: Dynamic Programming, Math, Memoization

Problem
-------
You are climbing a staircase that takes `n` steps to reach the top. Each
time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Constraints: 1 <= n <= 45.

Approach — the canonical 1-D DP
-------------------------------
Let f(n) = number of distinct ways to reach step n. The last move into
step n is either:
  - a single step from n-1, or
  - a double step from n-2.
So f(n) = f(n-1) + f(n-2), with base cases f(1) = 1 and f(2) = 2.

That's Fibonacci with a different starting pair. The "rolling two
variables" trick collapses the O(n) table to O(1) extra space — we never
need anything older than the previous two values.

Complexity
----------
Time:  O(n)   — one addition per step from 3..n.
Space: O(1)   — two scalars `prev` and `curr` hold all the state we need.

Why iterative bottom-up beats recursion here
--------------------------------------------
Pure recursion `climb(n) = climb(n-1) + climb(n-2)` is O(2^n) — the same
exponential blowup as naive Fibonacci. Memoization fixes it to O(n) but
adds dict/lru_cache overhead and uses O(n) stack. The bottom-up rewrite
is the same O(n) work without either cost — the textbook DP recipe in
its smallest form.
"""

from typing import List  # noqa: F401  (kept for LeetCode-template parity)


class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases handled directly so the loop body stays clean.
        if n <= 2:
            return n
        # prev = f(i-2), curr = f(i-1). Start i at 3.
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr


# ---------------------------------------------------------------------------
# Local test block — NOT copied to LeetCode. The class above is the
# LeetCode submission; everything below stays in the repo.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Sanity table: classic Fibonacci-shift sequence.
    # n:   1  2  3  4  5  6   7   8   9  10
    # f(n):1  2  3  5  8  13  21  34  55  89
    cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
        # LeetCode-provided examples.
        (2, 2),
        (3, 3),
        # Upper boundary in the constraints.
        (45, 1_836_311_903),
        # One step before the upper boundary.
        (44, 1_134_903_170),
    ]

    for n, expected in cases:
        got = sol.climbStairs(n)
        assert got == expected, f"FAIL n={n}: expected {expected}, got {got}"
        print(f"  n={n:<3} -> {got}  (expected {expected})  OK")

    print("All tests passed.")
