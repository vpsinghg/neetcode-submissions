# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False
        
        is_equal = root.val == subRoot.val
        if not is_equal:
            return False

        return self.isSame(root.left,subRoot.left) and self.isSame(root.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False
        
        is_equal = self.isSame(root,subRoot)

        if is_equal:
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        