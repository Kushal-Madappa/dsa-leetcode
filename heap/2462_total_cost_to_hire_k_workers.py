# LeetCode: Total Cost to Hire K Workers (#2462)
# https://leetcode.com/problems/total-cost-to-hire-k-workers/
from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if 2 * candidates >= n:
            return sum(sorted(costs)[:k])
        left = costs[:candidates]
        right = costs[n - candidates:]
        heapq.heapify(left)
        heapq.heapify(right)
        i = candidates
        j = n - candidates - 1
        total = 0
        for _ in range(k):
            if not right or (left and left[0] <= right[0]):
                total += heapq.heappop(left)
                if i <= j:
                    heapq.heappush(left, costs[i])
                    i += 1
            else:
                total += heapq.heappop(right)
                if i <= j:
                    heapq.heappush(right, costs[j])
                    j -= 1
        return total
