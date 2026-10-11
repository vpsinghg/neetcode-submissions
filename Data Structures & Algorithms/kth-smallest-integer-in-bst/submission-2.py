# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1
            left = dfs(root.left)
            if left != -1:
                return left
            nonlocal index
            index += 1
            if index == k:
                return root.val

            return dfs(root.right)

        return dfs(root)
