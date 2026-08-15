# LeetCode: Unique Number of Occurrences (#1207)
# https://leetcode.com/problems/unique-number-of-occurrences/
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))
