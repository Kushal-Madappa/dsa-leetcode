"""
LeetCode #377 — Combination Sum IV  (Medium)

Topics: Dynamic Programming, Unbounded Knapsack (counting), 1-D DP

Problem
-------
Given an array of distinct positive integers `nums` and a non-negative
integer `target`, return the number of *ordered* sequences (a.k.a.
permutations) of elements drawn from `nums` (with repetition) whose
elements sum to `target`.

Note (deceptive name): despite being called "Combination" Sum IV, the
problem actually counts **permutations** — `[1, 2]` and `[2, 1]` are
counted separately. That is the entire point of the loop-order choice
below.

Approach — outer amount, inner coins (permutation count)
--------------------------------------------------------
This is the mirror of LeetCode #518 (Coin Change II), which counts
*unordered* combinations using outer-coins / inner-amount. Same
recurrence body — what changes is the nesting:

    for a in 1..target:
        for c in nums:
            if c <= a:
                dp[a] += dp[a - c]

When we update `dp[a]` for a specific `a`, every right-hand `dp[a - c]`
already represents "ways to make `a - c` using *any* coin appearing as
the last addition." So the same multiset is reached once per
last-element choice — which is exactly the permutation count.

Why dp[0] = 1
-------------
The empty sequence sums to 0 in exactly one way. Forgetting this seed
zeros out every `dp[a]` and the function returns 0.

Complexity
----------
Time:  O(target * len(nums))
Space: O(target)
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[a] = number of ordered sequences of elements of `nums`
        # (with repetition) that sum to a.
        dp = [0] * (target + 1)
        dp[0] = 1  # empty sequence -> the one way to make 0

        # Outer = amount, inner = coins  =>  counts PERMUTATIONS.
        # (Swap the loops to count combinations, as in #518.)
        for a in range(1, target + 1):
            for c in nums:
                if c <= a:
                    dp[a] += dp[a - c]

        return dp[target]


# ------------------------------------------------------------------
# Local test harness — runs only when this file is executed directly.
# Paste the class above into LeetCode; leave this block here locally.
# ------------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    cases = [
        # (nums, target, expected)
        # ---- LeetCode official samples ----
        ([1, 2, 3], 4, 7),            # 1111, 112, 121, 211, 22, 13, 31
        ([9], 3, 0),                  # cannot reach 3 with only {9}
        # ---- Edge cases ----
        ([1, 2, 3], 0, 1),            # empty sequence is the lone way
        ([1], 1, 1),                  # the only sequence is [1]
        ([1], 5, 1),                  # [1,1,1,1,1] is the only sequence
        ([2], 5, 0),                  # parity-unreachable
        ([2], 6, 1),                  # [2,2,2]
        # ---- Larger / stress ----
        ([1, 2, 3], 10, 274),         # known reference value
        ([2, 3, 5], 8, 6),
        # Permutation vs combination contrast:
        # for nums=[1,2,5], target=5, COMBINATIONS = 4 (i.e. {5},
        # {2,2,1}, {2,1,1,1}, {1,1,1,1,1}); PERMUTATIONS = 9.
        ([1, 2, 5], 5, 9),
    ]

    all_pass = True
    for nums, target, expected in cases:
        got = sol.combinationSum4(list(nums), target)
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            all_pass = False
        print(f"  [{status}]  nums={nums}, target={target}  ->  "
              f"got={got}, expected={expected}")

    print()
    print("All tests passed." if all_pass else "Some tests FAILED.")
