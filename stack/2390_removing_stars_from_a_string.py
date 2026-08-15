# LeetCode: Removing Stars From a String (#2390)
# https://leetcode.com/problems/removing-stars-from-a-string/


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
