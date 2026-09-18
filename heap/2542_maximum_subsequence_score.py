# LeetCode: Maximum Subsequence Score (#2542)
# https://leetcode.com/problems/maximum-subsequence-score/
import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        heap = []
        s = 0
        best = 0
        for a, b in pairs:
            heapq.heappush(heap, a)
            s += a
            if len(heap) > k:
                s -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, s * b)
        return best
