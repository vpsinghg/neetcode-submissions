# Definition for a binary tree node.
# class TreeNode:
import queue
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        levels = []

        while len(queue):
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()

                level.append(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

            levels.append(level)

        return levels
