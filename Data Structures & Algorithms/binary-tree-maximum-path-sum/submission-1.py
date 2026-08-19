class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through this node
            curr_sum = node.val + left + right

            max_path_sum = max(max_path_sum, curr_sum)

            # Path going upward to parent
            return node.val + max(left, right)

        dfs(root)
        return max_path_sum