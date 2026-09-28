# LeetCode: Remove Duplicates from Sorted List II (#82)
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                dup = cur.val
                while cur and cur.val == dup:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next
