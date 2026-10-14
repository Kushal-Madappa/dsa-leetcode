# LeetCode: Count Complete Tree Nodes (#222)
# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional['TreeNode']) -> int:
        if root is None:
            return 0
        lh, rh = 0, 0
        n = root
        while n:
            lh += 1
            n = n.left
        n = root
        while n:
            rh += 1
            n = n.right
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
