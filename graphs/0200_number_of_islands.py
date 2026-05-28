"""
LeetCode 200 — Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid `grid` of '1's (land) and '0's (water), return
the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically (4-directional). Cells
outside the grid are treated as water.

Examples
--------
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]  -> 1

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]  -> 3

Approach
--------
Linear scan; whenever we hit an unvisited '1', that's a new island, so
increment the counter and run a flood fill that marks the whole connected
component as visited. Marking is done *in place* by overwriting the visited
cells with '0' — no separate visited set is needed, and we visit each cell
at most twice (once by the outer loop, once by the flood fill). The flood
fill uses an explicit deque-based DFS so we do not blow the recursion
stack on a giant island (LeetCode grids can be 300x300; a recursive DFS
can hit Python's default limit on the worst-case spiral).

Complexity
----------
Time  O(m * n) — each cell is pushed/popped at most once.
Space O(m * n) — worst case the stack holds a long snake-shaped island.
"""

from collections import deque
from typing import List


# ── LeetCode submission (copy ONLY the class below into the LC editor) ──
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] != "1":
                    continue
                # New island found — flood fill it with iterative DFS.
                count += 1
                stack = deque([(r, c)])
                grid[r][c] = "0"  # mark as visited immediately
                while stack:
                    x, y = stack.pop()
                    for dx, dy in DIRS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            stack.append((nx, ny))
        return count


# ─────────────────────── local tests (not submitted) ────────────────────
if __name__ == "__main__":
    def run(grid):
        # Solution mutates the grid in place, so copy before each run.
        return Solution().numIslands([row[:] for row in grid])

    # LC sample 1: one big island
    g1 = [["1", "1", "1", "1", "0"],
          ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]]
    assert run(g1) == 1, run(g1)

    # LC sample 2: three islands
    g2 = [["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]]
    assert run(g2) == 3, run(g2)

    # All water
    assert run([["0", "0"], ["0", "0"]]) == 0

    # All land — connected as one island
    assert run([["1", "1"], ["1", "1"]]) == 1

    # Single cell — land
    assert run([["1"]]) == 1

    # Single cell — water
    assert run([["0"]]) == 0

    # Empty grid (defensive)
    assert run([]) == 0
    assert run([[]]) == 0

    # Diagonal islands should NOT connect (only 4-directional counts).
    # Grid has 3 + 2 + 3 = 8 land cells, all isolated -> 8 islands.
    diag = [["1", "0", "1", "0", "1"],
            ["0", "1", "0", "1", "0"],
            ["1", "0", "1", "0", "1"]]
    assert run(diag) == 8, run(diag)

    # Single column snake (stress the iterative DFS — no recursion blow-up)
    snake = [["1"]] * 1000  # 1000 rows, 1 col, all '1'
    assert run(snake) == 1

    # Ring of land around water — one island (water in middle doesn't matter)
    ring = [["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]]
    assert run(ring) == 1

    # Donut + interior island
    donut = [["1", "1", "1", "1", "1"],
             ["1", "0", "0", "0", "1"],
             ["1", "0", "1", "0", "1"],
             ["1", "0", "0", "0", "1"],
             ["1", "1", "1", "1", "1"]]
    assert run(donut) == 2  # outer ring + interior single cell

    # Long L-shape — still one island
    L = [["1", "0", "0"],
         ["1", "0", "0"],
         ["1", "1", "1"]]
    assert run(L) == 1

    # Two separate L-shapes
    twoL = [["1", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "1"],
            ["1", "1", "0", "1", "1"]]
    assert run(twoL) == 2

    print("All tests passed.")
