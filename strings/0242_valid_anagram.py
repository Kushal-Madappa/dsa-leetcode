"""
LeetCode 242: Valid Anagram
Difficulty: Easy
Topics: Hash Table, String, Sorting

Problem
-------
Given two strings s and t, return True if t is an anagram of s, otherwise
False. An anagram is a rearrangement of all the letters of the original
string, using each letter exactly once.

Example
-------
    Input:  s = "anagram", t = "nagaram"
    Output: True

    Input:  s = "rat", t = "car"
    Output: False

Approaches
----------
A. Sorting:
       return sorted(s) == sorted(t)
   Simple, correct, but O(n log n) time.

B. Counting (preferred):
   Build a frequency map from s, then decrement using t. If any count goes
   negative, t has a letter s doesn't (or too many of one letter).

C. Counter shortcut (Pythonic):
       return Counter(s) == Counter(t)
   Same big-O as (B); very readable.

Complexity (counting)
---------------------
    Time:  O(n)  -- one pass through each string.
    Space: O(k)  -- k = distinct characters (<= 26 for lowercase a-z).
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts: dict[str, int] = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if ch not in counts or counts[ch] == 0:
                return False
            counts[ch] -= 1
        return True

    # Idiomatic one-liner -- great for production code, fine for interviews
    # once you've shown you understand the underlying idea.
    def isAnagram_pythonic(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()

    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("", "") is True
    assert sol.isAnagram("a", "ab") is False
    assert sol.isAnagram("aacc", "ccac") is False  # same letters, wrong counts

    # Pythonic variant should match
    assert sol.isAnagram_pythonic("listen", "silent") is True
    assert sol.isAnagram_pythonic("hello", "world") is False

    print("All tests passed.")
