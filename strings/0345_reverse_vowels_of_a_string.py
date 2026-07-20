# LeetCode: Reverse Vowels of a String (#345)
# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            if chars[i] not in vowels:
                i += 1
                continue
            if chars[j] not in vowels:
                j -= 1
                continue
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return "".join(chars)
