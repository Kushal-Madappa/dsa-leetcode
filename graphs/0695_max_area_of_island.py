# LeetCode: Max Area of Island (#695)
# https://leetcode.com/problems/max-area-of-island/

from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r0 in range(rows):
            for c0 in range(cols):
                if grid[r0][c0] != 1:
                    continue
                # Iterative DFS — mark visited in place to avoid an O(m*n)
                # visited set and to sidestep Python's recursion limit on
                # long snake-shaped islands (up to 50*50 = 2500 cells).
                stack = deque()
                stack.append((r0, c0))
                grid[r0][c0] = 0
                area = 0
                while stack:
                    r, c = stack.pop()
                    area += 1
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                if area > best:
                    best = area
        return best
