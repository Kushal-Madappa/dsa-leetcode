# LeetCode: Longest Common Subsequence (#1143)
# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # dp[j] holds LCS length for text1[:i] vs text2[:j]; rolling 1D array.
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            ci = text1[i - 1]
            for j in range(1, n + 1):
                if ci == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[n]
