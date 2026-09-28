# LeetCode: Substring with Concatenation of All Words (#30)
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not words[0]:
            return []
        word_len = len(words[0])
        k = len(words)
        total = word_len * k
        n = len(s)
        if n < total:
            return []
        need = Counter(words)
        result = []
        # Try each offset from 0..word_len-1; sliding window of k words
        for offset in range(word_len):
            left = offset
            count = 0
            window = defaultdict(int)
            for right in range(offset, n - word_len + 1, word_len):
                w = s[right:right + word_len]
                if w in need:
                    window[w] += 1
                    count += 1
                    while window[w] > need[w]:
                        lw = s[left:left + word_len]
                        window[lw] -= 1
                        count -= 1
                        left += word_len
                    if count == k:
                        result.append(left)
                        # Shrink one word to continue
                        lw = s[left:left + word_len]
                        window[lw] -= 1
                        count -= 1
                        left += word_len
                else:
                    window.clear()
                    count = 0
                    left = right + word_len
        return result
