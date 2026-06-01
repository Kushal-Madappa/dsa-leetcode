# LeetCode: Find if Path Exists in Graph (#1971)
# https://leetcode.com/problems/find-if-path-exists-in-graph/
from typing import List
from collections import defaultdict, deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = {source}
        q = deque([source])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei == destination:
                    return True
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return False
