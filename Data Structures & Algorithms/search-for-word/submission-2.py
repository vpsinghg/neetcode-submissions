class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        word_length = len(word)
        visited = [[False] * COLS for _ in range(ROWS)]
        visiting = set()

        def dfs(i: int, j: int, curr_word: str):
            # store exploring
            nonlocal visiting

            if i < 0 or j < 0 or i >= ROWS or j >= COLS or len(curr_word) > word_length or (i,j) in visiting:
                return False

            visiting.add((i,j))
            curr_word += board[i][j]

            if curr_word == word:
                return True


            # explore all sides
            left = dfs(i, j - 1, curr_word)

            if left:
                return True

            top = dfs(i - 1, j, curr_word)

            if top:
                return True

            right = dfs(i, j + 1, curr_word)

            if right:
                return True

            bottom = dfs(i + 1, j, curr_word)

            if bottom:
                return True

            visiting.remove((i,j))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                visiting = set()
                if dfs(i, j, ""):
                    return True

        return False
