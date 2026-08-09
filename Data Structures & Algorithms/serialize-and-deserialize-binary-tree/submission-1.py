# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return "#".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split("#")

        if not arr or arr[0] == "null":
            return None

        root = TreeNode(int(arr[0]))
        queue = deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            # Left child
            if arr[i] != "null":
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)

            i += 1

            # Right child
            if arr[i] != "null":
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)

            i += 1

        return root
