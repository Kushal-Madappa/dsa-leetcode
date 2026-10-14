# LeetCode: Sum Root to Leaf Numbers (#129)
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if node is None:
                return 0
            cur = cur * 10 + node.val
            if node.left is None and node.right is None:
                return cur
            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)
