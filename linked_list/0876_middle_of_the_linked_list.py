# LeetCode: Middle of the Linked List (#876)
# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


class Solution:
    def middleNode(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
