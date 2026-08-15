# LeetCode: Maximum Twin Sum of a Linked List (#2130)
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
from typing import Optional


class Solution:
    def pairSum(self, head: Optional["ListNode"]) -> int:
        # 1) Find middle with slow/fast pointers.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half starting at `slow`.
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3) Walk first half and reversed second half, track max sum.
        best = 0
        left, right = head, prev
        while right:
            best = max(best, left.val + right.val)
            left = left.next
            right = right.next
        return best
