# LeetCode: Delete the Middle Node of a Linked List (#2095)
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
