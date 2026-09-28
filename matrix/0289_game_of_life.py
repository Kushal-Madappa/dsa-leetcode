# LeetCode: Game of Life (#289)
# https://leetcode.com/problems/game-of-life/
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]
        # Encode: bit 0 = current state, bit 1 = next state
        for i in range(m):
            for j in range(n):
                live = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] & 1) == 1:
                        live += 1
                if (board[i][j] & 1) == 1 and (live == 2 or live == 3):
                    board[i][j] |= 2
                elif (board[i][j] & 1) == 0 and live == 3:
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
