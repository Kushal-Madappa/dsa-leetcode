# LeetCode: Island Perimeter (#463)
# https://leetcode.com/problems/island-perimeter/
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Each land cell contributes 4 to the perimeter; every shared edge
        with a previously-seen neighbour (above or left) cancels 2 (one
        side per cell). Scanning top-to-bottom, left-to-right counts each
        shared edge exactly once.

        Time:  O(m * n)
        Space: O(1)
        """
        m, n = len(grid), len(grid[0])
        perim = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perim += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perim -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perim -= 2
        return perim
