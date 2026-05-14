"""
LeetCode 49: Group Anagrams
Difficulty: Medium
Topics: Hash Table, String, Sorting, Categorization

Problem
-------
Given an array of strings `strs`, group the anagrams together. Return the
groups in any order, and the strings within a group in any order.

Two strings are anagrams iff they contain the exact same letters with the
exact same frequencies.

Example
-------
    Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Approach
--------
The "categorization" trick: design a canonical key that two strings share
iff they are anagrams. Then bucket strings by that key.

Two natural keys:

1. Sorted-letters key, O(n * k log k):
       key = "".join(sorted(s))
   Easy to write, slightly slower because of the sort per string.

2. Letter-frequency key (chosen here), O(n * k):
       key = (count_a, count_b, ..., count_z)
   We tally letters in O(k) and use the tuple as a dict key. Asymptotically
   faster when strings are long and the alphabet is fixed (lowercase English).

Either is acceptable in an interview; mentioning the trade is the point.

Complexity (frequency-key version)
----------------------------------
    Let n = number of strings, k = max string length.
    Time:  O(n * k)  -- one O(k) pass per string to build its key.
    Space: O(n * k)  -- output groups plus the dict of keys.

Why this matters
----------------
"Hash by a canonical fingerprint" is one of the most reusable hashing
patterns. You will see it again for: grouping by sum of digits, by signed
slope (collinear points), by sorted character multiset, etc.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets: dict[tuple, list[str]] = defaultdict(list)
        for s in strs:
            counts = [0] * 26  # fixed-size alphabet -> tuple is hashable & fast
            for ch in s:
                counts[ord(ch) - ord("a")] += 1
            buckets[tuple(counts)].append(s)
        return list(buckets.values())


def _normalize(groups: List[List[str]]) -> List[List[str]]:
    """Sort within each group and across groups so we can compare results."""
    return sorted([sorted(g) for g in groups])


if __name__ == "__main__":
    sol = Solution()

    # Standard example
    out = _normalize(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    assert out == _normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    # Empty string is its own group
    out = _normalize(sol.groupAnagrams([""]))
    assert out == [[""]]

    # Single string
    out = _normalize(sol.groupAnagrams(["a"]))
    assert out == [["a"]]

    # All identical -> one bucket
    out = _normalize(sol.groupAnagrams(["abc", "bca", "cab"]))
    assert out == [["abc", "bca", "cab"]]

    # All distinct anagram classes
    out = _normalize(sol.groupAnagrams(["abc", "def", "ghi"]))
    assert out == _normalize([["abc"], ["def"], ["ghi"]])

    print("All tests passed.")
