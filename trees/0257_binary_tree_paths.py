# LeetCode: Binary Tree Paths (#257)
# https://leetcode.com/problems/binary-tree-paths/
from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional["TreeNode"]) -> List[str]:
        paths = []

        def dfs(node, path):
            if node is None:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                paths.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return paths
