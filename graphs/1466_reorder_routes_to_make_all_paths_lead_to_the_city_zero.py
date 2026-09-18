# LeetCode: Reorder Routes to Make All Paths Lead to the City Zero (#1466)
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
from typing import List
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # original a->b: costs 1 to flip toward 0
            graph[b].append((a, 0))  # reverse edge: already toward 0
        visited = [False] * n
        visited[0] = True
        count = 0
        q = deque([0])
        while q:
            node = q.popleft()
            for nei, cost in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    count += cost
                    q.append(nei)
        return count
