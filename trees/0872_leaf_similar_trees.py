# LeetCode: Leaf-Similar Trees (#872)
# https://leetcode.com/problems/leaf-similar-trees/
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional['TreeNode'], root2: Optional['TreeNode']) -> bool:
        def leaves(node, out: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                out.append(node.val)
                return
            leaves(node.left, out)
            leaves(node.right, out)

        a, b = [], []
        leaves(root1, a)
        leaves(root2, b)
        return a == b
