# LeetCode: Kids With the Greatest Number of Candies (#1431)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
