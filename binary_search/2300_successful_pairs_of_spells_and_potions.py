# LeetCode: Successful Pairs of Spells and Potions (#2300)
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            # need potion >= ceil(success / s)
            threshold = (success + s - 1) // s
            idx = bisect_left(potions, threshold)
            res.append(m - idx)
        return res
