# LeetCode: Equal Row and Column Pairs (#2352)
# https://leetcode.com/problems/equal-row-and-column-pairs/
from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        n = len(grid)
        count = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += row_counts[col]
        return count
