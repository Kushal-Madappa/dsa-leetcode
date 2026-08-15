# LeetCode: Palindrome Linked List (#234)
# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional["ListNode"]) -> bool:
        # Find middle with slow/fast pointers.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in place.
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare halves.
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
