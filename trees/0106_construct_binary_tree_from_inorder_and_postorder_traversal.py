# LeetCode: Construct Binary Tree from Inorder and Postorder Traversal (#106)
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        self.p = len(postorder) - 1

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            val = postorder[self.p]
            self.p -= 1
            node = TreeNode(val)
            mid = idx[val]
            node.right = build(mid + 1, hi)
            node.left = build(lo, mid - 1)
            return node

        return build(0, len(inorder) - 1)
