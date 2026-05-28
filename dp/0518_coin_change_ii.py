# LeetCode 518 — Coin Change II
# https://leetcode.com/problems/coin-change-ii/
#
# Medium. Topic: Dynamic Programming (unbounded knapsack — count of ways).
#
# Given an integer `amount` and an array of distinct coin denominations
# `coins`, return the number of *combinations* that make up that amount.
# Each coin may be used an unlimited number of times. Returns 0 if no
# combination is possible. Guaranteed answer fits in a signed 32-bit int.
#
# Core insight (the loop-order lesson):
#   `dp[a]` = number of combinations to make amount `a` using the coins
#   considered so far.  Iterate OUTER over `coins`, INNER over `amount`.
#     dp[0] = 1   (one way to make zero: pick nothing)
#     for c in coins:
#         for a in range(c, amount + 1):
#             dp[a] += dp[a - c]
#
# Why this loop order counts combinations (not permutations):
#   Fixing the coin order in the outer loop means that when we process
#   coin `c`, every combination we build appends `c`s to an existing
#   combination that uses only earlier coins (or zero copies of them).
#   So a single multiset {1, 2, 2} is counted once, no matter the order
#   the coins are "placed".
#
# If we swapped the loops (OUTER amount, INNER coins) we would count
# permutations: {1, 2, 2}, {2, 1, 2}, {2, 2, 1} would each tally separately.
# That is the right shape for "climb stairs taking step sizes from a set"
# but the wrong shape for coin-change-II.
#
# Complexity: Time O(amount × len(coins)), Space O(amount).

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        return dp[amount]


if __name__ == "__main__":
    s = Solution()

    cases = [
        # (amount, coins, expected, label)
        (5,  [1, 2, 5],            4,   "LC sample 1 — {5},{2,2,1},{2,1,1,1},{1,1,1,1,1}"),
        (3,  [2],                  0,   "LC sample 2 — unreachable"),
        (10, [10],                 1,   "LC sample 3 — single-coin exact"),
        (0,  [1, 2, 5],            1,   "amount=0 — empty multiset counts once"),
        (1,  [1, 2, 5],            1,   "amount=1 — only {1}"),
        (4,  [1, 2, 3],            4,   "{1*4},{1*2+2},{2+2},{1+3}"),
        (500, [1, 2, 5],           12701, "stress — must stay int, no overflow"),
        (7,  [2, 4],               0,   "parity-unreachable (all coins even)"),
        (6,  [1, 3, 4],            4,   "{1*6},{1*3+3},{3+3},{1*2+4}"),
        (5,  [1, 2, 5],            4,   "duplicate of sample 1 to be safe"),
        (11, [9, 6, 5, 1],         6,   "mixed denoms — {1*11},{5,1*6},{5,5,1},{6,1*5},{6,5},{9,1,1}"),
        (0,  [],                   1,   "amount=0, empty coins — still one way (pick nothing)"),
        (5,  [],                   0,   "amount>0, empty coins — zero ways"),
    ]

    all_ok = True
    for i, (amt, cs, exp, label) in enumerate(cases, 1):
        got = s.change(amt, cs)
        status = "PASS" if got == exp else "FAIL"
        if got != exp:
            all_ok = False
        print(f"Case {i:>2}: amount={amt}, coins={cs} -> {got} (expected {exp}) [{status}]  {label}")

    print()
    print("All tests passed." if all_ok else "SOME TESTS FAILED.")
