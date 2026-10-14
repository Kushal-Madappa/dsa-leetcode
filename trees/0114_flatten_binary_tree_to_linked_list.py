# LeetCode: Flatten Binary Tree to Linked List (#114)
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                # Find rightmost node of left subtree
                rightmost = cur.left
                while rightmost.right:
                    rightmost = rightmost.right
                # Rewire: left subtree becomes right subtree
                rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
