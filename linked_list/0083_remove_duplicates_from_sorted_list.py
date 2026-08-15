# LeetCode: Remove Duplicates from Sorted List (#83)
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
