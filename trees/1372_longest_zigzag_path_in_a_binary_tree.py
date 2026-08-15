# LeetCode: Longest ZigZag Path in a Binary Tree (#1372)
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional['TreeNode']) -> int:
        self.best = 0

        # returns (left_len, right_len): longest zigzag path length starting
        # by going left / right from this node (edge counts).
        def dfs(node):
            if not node:
                return -1, -1
            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            left_len = lr + 1   # step to left child, then continue from its right
            right_len = rl + 1  # step to right child, then continue from its left
            self.best = max(self.best, left_len, right_len)
            return left_len, right_len

        dfs(root)
        return self.best
