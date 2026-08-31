class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        visited = [ False for _ in range(n)]

        def dfs(node: int):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        count = 0

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count