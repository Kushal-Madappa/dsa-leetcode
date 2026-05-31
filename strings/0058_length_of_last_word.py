# LeetCode: Length of Last Word (#58)
# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Walk from the right: skip trailing spaces, then count non-space
        characters until the next space (or start of string). Single pass,
        no extra allocations.

        Time:  O(n)
        Space: O(1)
        """
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
