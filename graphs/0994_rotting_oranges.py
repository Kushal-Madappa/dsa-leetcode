"""
LeetCode 994 — Rotting Oranges (Medium)
https://leetcode.com/problems/rotting-oranges/

You are given an `m x n` `grid` where each cell can have one of three values:
    0 — empty,
    1 — fresh orange,
    2 — rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten. Return the minimum number of minutes that must elapse
until no cell has a fresh orange. If this is impossible, return -1.

Examples
--------
[[2,1,1],[1,1,0],[0,1,1]]                                -> 4
[[2,1,1],[0,1,1],[1,0,1]]                                -> -1 (bottom-left is unreachable)
[[0,2]]                                                  -> 0 (no fresh oranges)

Approach — multi-source BFS
---------------------------
This is the first problem in the graphs track that *requires* BFS rather than
DFS, because the question "how many minutes" is a shortest-time query and BFS
gives us shortest paths from the source set for free.

Two twists relative to single-source BFS:

  1. **Multiple sources.** Every initially-rotten cell starts at time 0. We
     seed the queue with *all* of them simultaneously. The BFS frontier then
     advances all rot fronts in lockstep — which is exactly the physical
     model "every minute, every rotten cell rots its neighbours."

  2. **Level-by-level processing.** We don't just want the BFS tree; we want
     the *depth* of the last cell visited. Two equivalent ways:
       - Store `(r, c, time)` triples and track the max time seen.
       - Process the queue one level at a time (snapshot len(queue) at the
         start of each iteration) and increment a `minutes` counter per level.
     I use the triple variant — it's slightly less code and the per-cell
     `time` falls out for free.

  3. **Unreachable fresh oranges => -1.** After the BFS terminates, if any
     `1` remains in the grid, those cells were never reached and the answer
     is `-1`. We track this by counting fresh oranges up front, then
     decrementing as each one rots; if `fresh > 0` at the end, return -1.

Complexity
----------
Time  O(m * n) — each cell enters the queue at most once.
Space O(m * n) — worst case the queue holds all cells (everything rotten at t=0).
"""

from collections import deque
from typing import List


# ── LeetCode submission (copy ONLY the class below into the LC editor) ──
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Seed: every rotten cell starts at time 0; count fresh cells.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        # Edge case: nothing fresh to rot — already done at minute 0.
        if fresh == 0:
            return 0

        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        elapsed = 0

        while queue:
            r, c, t = queue.popleft()
            elapsed = t  # last-popped time = current frontier depth
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2          # rot it (acts as visited mark)
                    fresh -= 1
                    queue.append((nr, nc, t + 1))

        return elapsed if fresh == 0 else -1


# ─────────────────────── local tests (not submitted) ────────────────────
if __name__ == "__main__":
    def run(grid):
        # Solution mutates the grid in place; copy each call.
        return Solution().orangesRotting([row[:] for row in grid])

    # LC sample 1
    assert run([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4

    # LC sample 2 — bottom-left fresh orange (row 2, col 0) is isolated by 0s
    assert run([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1

    # LC sample 3 — no fresh oranges; already at minute 0
    assert run([[0, 2]]) == 0

    # All empty
    assert run([[0, 0], [0, 0]]) == 0

    # All rotten — minute 0
    assert run([[2, 2], [2, 2]]) == 0

    # Single fresh, single rotten, adjacent — one minute
    assert run([[2, 1]]) == 1

    # Single fresh, no rotten — impossible
    assert run([[1]]) == -1

    # Single rotten — already done
    assert run([[2]]) == 0

    # Single empty cell
    assert run([[0]]) == 0

    # Long chain — 1 rotten at left end, 9 fresh — 9 minutes
    assert run([[2, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 9

    # Multi-source acceleration — two rotten at opposite ends of a chain of 10.
    # Without multi-source BFS, you'd get 9; with multi-source, the fronts
    # meet in the middle at minute ceil((n-2)/2) = 4.
    assert run([[2, 1, 1, 1, 1, 1, 1, 1, 1, 2]]) == 4

    # Diagonal is NOT considered adjacent — the lone fresh is unreachable.
    assert run([[2, 0, 0], [0, 1, 0], [0, 0, 2]]) == -1

    # Larger grid — 5x5 with one rotten in the center, surrounded by fresh.
    # The corner is Manhattan-distance 4 from center => 4 minutes.
    grid_5 = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 2, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]]
    assert run(grid_5) == 4

    # Rotten in corner of 3x3 all-fresh — opposite corner is 4 minutes away.
    assert run([[2, 1, 1], [1, 1, 1], [1, 1, 1]]) == 4

    print("All tests passed.")
