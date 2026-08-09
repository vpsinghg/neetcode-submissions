class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col):
            if visited[row][col]:
                return

            visited[row][col] = True
            dirs = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]

            for x, y in dirs:
                new_row = row + x
                new_col = col + y

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == "1"
                    and not visited[new_row][new_col]
                ):
                    dfs(new_row, new_col)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    islands += 1


        return islands
