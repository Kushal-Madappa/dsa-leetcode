# LeetCode: Sum of Left Leaves (#404)
# https://leetcode.com/problems/sum-of-left-leaves/
from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional["TreeNode"]) -> int:
        def dfs(node, is_left):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
