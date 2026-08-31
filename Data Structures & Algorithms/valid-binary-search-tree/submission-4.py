# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        

        curr = root
        prev = None

        while(curr):
            if curr.left is None:
                print(prev, curr.val)
                if(prev is not None and curr.val<=prev):
                    return False
                prev = curr.val
                curr = curr.right
            else:
                predecessor = curr.left

                while(predecessor.right and predecessor.right !=curr):
                    predecessor = predecessor.right
                
                # no link from predecessor -> curr
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None

                    if(prev and curr.val<=prev):
                        return False
                    prev = curr.val
                    curr = curr.right

        return True

        