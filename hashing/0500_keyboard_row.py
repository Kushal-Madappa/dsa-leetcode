# LeetCode: Keyboard Row (#500)
# https://leetcode.com/problems/keyboard-row/
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result = []
        for w in words:
            letters = set(w.lower())
            if any(letters <= row for row in rows):
                result.append(w)
        return result
