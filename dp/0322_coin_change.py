"""
LeetCode 322 — Coin Change (Medium)

You are given an integer array `coins` (denominations, any duplicates removed)
and an integer `amount`. Return the *fewest* number of coins needed to make up
that amount. If it is impossible, return -1.

Topics: Dynamic Programming (unbounded knapsack), 1-D DP over target

Approach — bottom-up DP over the target amount
-----------------------------------------------
State:        dp[a] = fewest coins needed to make exactly amount `a`
Base case:    dp[0] = 0  (zero coins make amount 0)
Init the rest: dp[a] = +infinity   (meaning "unreachable so far")
Transition:   dp[a] = min(dp[a - c] + 1) over every coin c with c <= a
Answer:       dp[amount] if it is finite, else -1

This is the canonical *unbounded* knapsack template: each coin can be used
any number of times, so the outer loop runs over the target `a` from 1 to
`amount` and the inner loop runs over every coin. Reusing a coin is implicit
because dp[a - c] may have already used that same coin.

Complexity
----------
Time:  O(amount * len(coins))
Space: O(amount)

Notes
-----
* Initialising with `amount + 1` (or `float('inf')`) is the standard
  "sentinel" trick — any real answer is at most `amount` (using all 1-coins,
  if 1 is available), so `amount + 1` cleanly marks "unreachable".
* Order of the inner loop does NOT matter for *min coins*; it only matters
  for *count of ways* (#518), where outer-loop-over-coins enforces that we
  don't double-count permutations.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Sentinel "unreachable" = amount + 1 (any real answer is at most `amount`)
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1

        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    s = Solution()

    cases = [
        # (coins, amount, expected)
        ([1, 2, 5], 11, 3),         # 5 + 5 + 1
        ([2], 3, -1),               # impossible
        ([1], 0, 0),                # zero amount → zero coins
        ([1], 1, 1),
        ([1], 2, 2),
        ([1, 2, 5], 0, 0),
        ([2, 5, 10, 1], 27, 4),     # 10+10+5+2
        ([186, 419, 83, 408], 6249, 20),  # classic LC tricky case
        ([1, 2147483647], 2, 2),    # large coin doesn't help
        ([3, 7, 405, 436], 8839, 25),
        ([2, 4], 7, -1),            # parity-unreachable target
        ([5, 7, 8], 0, 0),
    ]

    for coins, amount, expected in cases:
        got = s.coinChange(coins, amount)
        status = "OK" if got == expected else "FAIL"
        print(f"[{status}] coins={coins!s:<28} amount={amount:<6} expected={expected:<4} got={got}")
        assert got == expected, (coins, amount, expected, got)

    print("All tests passed.")
