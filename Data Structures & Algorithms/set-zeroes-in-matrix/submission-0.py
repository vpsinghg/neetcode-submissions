class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Check if first row or first column originally contains a zero
        first_row_zero = False
        first_col_zero = False

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Step 2: Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 5: Zero the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0