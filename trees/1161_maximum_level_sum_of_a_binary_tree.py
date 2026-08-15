# LeetCode: Maximum Level Sum of a Binary Tree (#1161)
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from typing import Optional
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional["TreeNode"]) -> int:
        best_level = 1
        best_sum = root.val
        level = 1
        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level
            level += 1
        return best_level
