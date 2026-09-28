# LeetCode: Reverse Nodes in k-Group (#25)
# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            group_next = kth.next

            # Reverse the group [group_prev.next ... kth]
            prev = group_next
            curr = group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
