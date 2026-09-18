# LeetCode: Evaluate Division (#399)
# https://leetcode.com/problems/evaluate-division/
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for nei, val in graph[src].items():
                if nei in visited:
                    continue
                sub = dfs(nei, dst, visited)
                if sub != -1.0:
                    return val * sub
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]
