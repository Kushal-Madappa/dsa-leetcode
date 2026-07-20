# LeetCode: First Unique Character in a String (#387)
# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
