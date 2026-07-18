# LeetCode: Find Center of Star Graph (#1791)
# https://leetcode.com/problems/find-center-of-star-graph/
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]
        return a if a == c or a == d else b
