# LeetCode: Nearest Exit from Entrance in Maze (#1926)
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        er, ec = entrance
        q = deque([(er, ec, 0)])
        visited = {(er, ec)}
        while q:
            r, c, d = q.popleft()
            if (r, c) != (er, ec) and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1
