# LeetCode: H-Index (#274)
# https://leetcode.com/problems/h-index/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        total = 0
        for h in range(n, -1, -1):
            total += buckets[h]
            if total >= h:
                return h
        return 0
