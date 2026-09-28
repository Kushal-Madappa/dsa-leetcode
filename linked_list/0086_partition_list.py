# LeetCode: Partition List (#86)
# https://leetcode.com/problems/partition-list/
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)
        b, a = before, after
        cur = head
        while cur:
            if cur.val < x:
                b.next = cur
                b = b.next
            else:
                a.next = cur
                a = a.next
            cur = cur.next
        a.next = None
        b.next = after.next
        return before.next
