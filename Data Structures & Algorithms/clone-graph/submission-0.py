"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(i_node):
            if i_node in clones:
                return clones[i_node]
            
            clone = Node(i_node.val)
            clones[i_node] = clone

            for neighbor in i_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node) if node else node

                