"""
LeetCode 509 — Fibonacci Number  (Easy)
Topics: Dynamic Programming, Math, Recursion, Memoization
Pattern: The canonical Fibonacci-shape DP — same skeleton as #70 (Climbing
Stairs) but with base case f(0)=0, f(1)=1 instead of f(1)=1, f(2)=2.

State:      f(n) = the n-th Fibonacci number
Transition: f(n) = f(n-1) + f(n-2)
Base:       f(0) = 0, f(1) = 1

Iterative two-variable rolling form keeps space at O(1).

Complexity: O(n) time, O(1) space.
"""


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev2, prev1 = 0, 1  # f(0), f(1)
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1


if __name__ == "__main__":
    s = Solution()
    # Reference table f(0)..f(20)
    table = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
             610, 987, 1597, 2584, 4181, 6765]
    for i, want in enumerate(table):
        got = s.fib(i)
        assert got == want, f"fib({i}) -> {got}, want {want}"
    # LC-provided examples
    assert s.fib(2) == 1
    assert s.fib(3) == 2
    assert s.fib(4) == 3
    # Upper boundary (LC constraint: 0 <= n <= 30)
    assert s.fib(30) == 832040
    print(f"All {len(table) + 4} tests passed.")
