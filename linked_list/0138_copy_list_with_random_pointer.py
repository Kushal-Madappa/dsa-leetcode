# LeetCode: Copy List with Random Pointer (#138)
# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            mapping[cur].next = mapping.get(cur.next)
            mapping[cur].random = mapping.get(cur.random)
            cur = cur.next
        return mapping[head]
