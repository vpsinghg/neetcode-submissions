# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0

        def dfs(root: Optional[TreeNode]):
            "Returns the heigh of the tree"
            nonlocal i

            if root is None:
                return -1

            val = dfs(root.left)
            if val != -1:
                return val
            i += 1
            if i == k:
                return root.val

            val = dfs(root.right)
            return val

        return dfs(root)
