# LeetCode: Repeated Substring Pattern (#459)
# https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Trick: s is built from a repeated substring iff s is a proper
        # substring of (s + s) with the first and last chars removed.
        return s in (s + s)[1:-1]
