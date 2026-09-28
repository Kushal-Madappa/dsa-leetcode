# LeetCode: Minimum Window Substring (#76)
# https://leetcode.com/problems/minimum-window-substring/
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        best_l, best_r = 0, -1
        best_len = len(s) + 1
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l, best_r = left, right
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return "" if best_r == -1 else s[best_l:best_r + 1]
