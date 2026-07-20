# LeetCode: Maximum Number of Vowels in a Substring of Given Length (#1456)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(1 for c in s[:k] if c in vowels)
        best = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            if count > best:
                best = count
        return best
