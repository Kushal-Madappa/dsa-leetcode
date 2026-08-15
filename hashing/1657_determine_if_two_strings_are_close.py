# LeetCode: Determine if Two Strings Are Close (#1657)
# https://leetcode.com/problems/determine-if-two-strings-are-close/
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        # Same set of characters (op 2 permits any relabelling within existing chars)
        if set(c1.keys()) != set(c2.keys()):
            return False
        # Same multiset of frequencies (op 1 permits any permutation of characters)
        return sorted(c1.values()) == sorted(c2.values())
