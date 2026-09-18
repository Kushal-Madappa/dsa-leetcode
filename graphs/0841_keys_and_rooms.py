# LeetCode: Keys and Rooms (#841)
# https://leetcode.com/problems/keys-and-rooms/
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [0]
        count = 1
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    count += 1
                    stack.append(key)
        return count == n
