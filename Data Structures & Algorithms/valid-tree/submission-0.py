class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = [[] for _ in range(n)]

        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n