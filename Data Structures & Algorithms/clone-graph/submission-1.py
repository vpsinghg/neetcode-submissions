"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        queue = deque([node])
        clone = Node(node.val)
        oldToNew[node] = clone

        # 
        while(queue):
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
            
                # add neighbors
                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]

        