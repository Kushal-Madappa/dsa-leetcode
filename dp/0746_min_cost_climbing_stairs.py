"""
LeetCode 746 — Min Cost Climbing Stairs  (Easy)
Topics: Dynamic Programming, Array
Pattern: 1-D DP, Fibonacci-shape recurrence with a cost per step.

You may start from index 0 or index 1.  Each step pays cost[i] to
*leave* that step, and you may move +1 or +2.  Reach "the top"
(index n, just past the array) with minimum total cost.

State:      f(i) = min cost to STAND on step i
Transition: f(i) = cost[i] + min(f(i-1), f(i-2))
Base:       f(0) = cost[0], f(1) = cost[1]   (free to start at either)
Answer:     min(f(n-1), f(n-2))              (the "top" is past the last step)

Two-variable rolling window again.

Complexity: O(n) time, O(1) space.
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost)              # free start, pay one step out
        prev2, prev1 = cost[0], cost[1]   # f(0), f(1)
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr
        return min(prev1, prev2)


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([10, 15, 20], 15),                                  # LC example 1
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),           # LC example 2
        ([0, 0, 0, 0], 0),                                   # everything free
        ([1, 2], 1),                                         # n=2 picks min
        ([10, 1], 1),                                        # n=2, second cheaper
        ([5, 5], 5),                                         # n=2, tie
        ([1, 2, 3], 2),                                      # start at 1, jump to top
        ([100, 1, 1, 100], 2),                               # 1 + 1 mid-path
        ([0, 2, 2, 1], 2),                                   # start 0 -> +2 -> +1 = 0+1=1?
                                                             # actually min(f(2),f(3))=min(2,2)=2
    ]
    for cost, want in cases:
        got = s.minCostClimbingStairs(cost)
        assert got == want, f"minCostClimbingStairs({cost}) -> {got}, want {want}"
    print(f"All {len(cases)} tests passed.")
