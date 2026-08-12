# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if node is None:
                return None

            # 1. Visit smaller values first
            result = dfs(node.left)

            if result is not None:
                return result

            # 2. Visit current node
            count += 1

            if count == k:
                return node.val

            # 3. Visit larger values
            return dfs(node.right)

        return dfs(root)