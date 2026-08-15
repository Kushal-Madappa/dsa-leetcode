# LeetCode: Linked List Cycle (#141)
# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional["ListNode"]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
