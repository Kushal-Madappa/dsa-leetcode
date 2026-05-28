# LeetCode: Ransom Note (#383)
# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for ch in ransomNote:
            if counts[ch] <= 0:
                return False
            counts[ch] -= 1
        return True
