# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node:Optional[TreeNode]):
            nonlocal max_path_sum
            if node is None:
                return float("-inf")
            
            left = dfs(node.left)
            right = dfs(node.right)

            curr_sum = node.val
            if left > 0:
                curr_sum += left
            if right > 0:
                curr_sum += right
            max_path_sum = max(max_path_sum,curr_sum)

            return max(node.val, left+node.val , right+node.val)

        dfs(root)        
        return max_path_sum
        