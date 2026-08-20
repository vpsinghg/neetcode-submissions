# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        hash_map = {}

        for i, val in enumerate(inorder):
            hash_map[val] = i

        def buildTreeUtil(
            preorder: List[int],
            inorder: List[int],
            pre_start: int,
            pre_end: int,
            inorder_start: int,
            inorder_end: int,
        ):
            if pre_start > pre_end or inorder_start > inorder_end:
                return None

            root_value = preorder[pre_start]
            root = TreeNode(root_value)
            if pre_start == pre_end:
                return root

            root_pos = hash_map[root_value]

            left_count = root_pos - inorder_start

            left = buildTreeUtil(
                preorder,
                inorder,
                pre_start + 1,
                pre_start + left_count,
                inorder_start,
                root_pos - 1,
            )

            right = buildTreeUtil(
                preorder, inorder, pre_start + left_count + 1, pre_end, root_pos + 1, inorder_end
            )

            root.left = left
            root.right = right
            return root

        return buildTreeUtil(preorder, inorder, 0, n - 1, 0, n - 1)
