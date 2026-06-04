"""
LeetCode 547 — Number of Provinces (Medium)

There are `n` cities. Some pairs are directly connected. A *province* is a
group of directly or indirectly connected cities — the connected components
of the city graph.

You are given an `n x n` adjacency matrix `isConnected` where
`isConnected[i][j] == 1` if city `i` and city `j` are directly connected,
and `0` otherwise. The matrix is symmetric (undirected graph) and the
diagonal is all 1s (each city is connected to itself).

Return the number of provinces (connected components).

Topics: Graph, DFS, Union-Find

Approach — iterative DFS over the adjacency matrix
--------------------------------------------------
This is the same connected-components-count engine as #200 Number of
Islands, but the graph is given as an *adjacency matrix* instead of a grid.
The "neighbours of node u" are now found by scanning row `isConnected[u]`
for `1`s, not by checking 4 cardinal directions on a grid.

State:
  visited[i] = True once node i has been claimed by some component

Procedure:
  For each city i from 0 to n-1:
      if not visited[i]:
          provinces += 1
          iterative DFS from i, marking everything reachable as visited

Complexity
----------
Time:  O(n^2) — every cell of the matrix is read at most twice (once when
       its row is scanned during DFS, once never since visited blocks revisits).
Space: O(n) — for `visited` and the explicit DFS stack.

Notes
-----
* Use an explicit stack (deque) instead of recursion. Python's default
  recursion limit (1000) is below the LeetCode upper bound n <= 200, but
  the constant factor of deep recursion is still wasteful and the
  defensive pattern keeps the solution portable.
* Union-Find is the canonical alternative. It is also O(n^2 * α(n)) here
  because we still have to iterate every off-diagonal pair. Same Big-O,
  more bookkeeping — DFS is the cleaner answer for #547 specifically.
"""

from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for start in range(n):
            if visited[start]:
                continue
            provinces += 1
            # Iterative DFS from `start`
            stack = deque([start])
            visited[start] = True
            while stack:
                u = stack.pop()
                row = isConnected[u]
                for v in range(n):
                    if row[v] == 1 and not visited[v]:
                        visited[v] = True
                        stack.append(v)

        return provinces


if __name__ == "__main__":
    s = Solution()

    cases = [
        # (isConnected, expected, label)
        ([[1, 1, 0],
          [1, 1, 0],
          [0, 0, 1]], 2, "LC example 1 — two provinces"),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 3, "LC example 2 — no edges, three provinces"),
        ([[1]], 1, "single city"),
        ([[1, 1],
          [1, 1]], 1, "two fully connected cities"),
        ([[1, 0],
          [0, 1]], 2, "two disconnected cities"),
        ([[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]], 1, "complete graph K4"),
        ([[1, 0, 0, 1],
          [0, 1, 1, 0],
          [0, 1, 1, 0],
          [1, 0, 0, 1]], 2, "two 2-cliques: {0,3}, {1,2}"),
        ([[1, 1, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 1]], 3, "three components: pair, pair, singleton"),
        # 200x200 line graph stress test (snake of edges) -> 1 province
        (
            [[1 if i == j or abs(i - j) == 1 else 0 for j in range(200)] for i in range(200)],
            1,
            "200x200 chain — single province, no recursion blow-up",
        ),
        # 200x200 identity -> 200 provinces (no edges)
        (
            [[1 if i == j else 0 for j in range(200)] for i in range(200)],
            200,
            "200x200 identity — 200 isolated cities",
        ),
    ]

    for matrix, expected, label in cases:
        got = s.findCircleNum(matrix)
        status = "OK" if got == expected else "FAIL"
        print(f"[{status}] {label:<55} expected={expected:<4} got={got}")
        assert got == expected, (label, expected, got)

    print("All tests passed.")
