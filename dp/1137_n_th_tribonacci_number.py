"""
LeetCode 1137 — N-th Tribonacci Number  (Easy)
Topics: Dynamic Programming, Math, Memoization
Pattern: Three-step lookback DP — extends the Fibonacci rolling-window
idea to a three-variable state.

State:      T(n) = the n-th Tribonacci number
Transition: T(n) = T(n-1) + T(n-2) + T(n-3)
Base:       T(0) = 0, T(1) = 1, T(2) = 1

Three rolling scalars hold the last three values.

Complexity: O(n) time, O(1) space.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1  # T(0), T(1), T(2)
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


if __name__ == "__main__":
    s = Solution()
    # T(0)..T(15)
    table = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136]
    for i, want in enumerate(table):
        got = s.tribonacci(i)
        assert got == want, f"tribonacci({i}) -> {got}, want {want}"
    # LC-provided examples
    assert s.tribonacci(4) == 4
    assert s.tribonacci(25) == 1389537
    # Upper boundary (LC constraint: 0 <= n <= 37)
    assert s.tribonacci(37) == 2082876103
    print(f"All {len(table) + 3} tests passed.")
