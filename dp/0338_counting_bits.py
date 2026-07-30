# LeetCode: Counting Bits (#338)
# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # dp[i] = dp[i >> 1] + (i & 1): drop the low bit, then add it back.
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
