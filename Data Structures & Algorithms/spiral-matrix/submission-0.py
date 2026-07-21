class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        # boundaries
        left = 0
        right = cols - 1
        top = 0
        bottom = rows - 1
        sol = []
        while left <= right and top <= bottom:
            # traverse from left to right
            for i in range(left, right + 1):
                sol.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                sol.append(matrix[i][right])
            right -= 1

            # right to left
            if top<=bottom:
                for i in range(right, left - 1, -1):
                    sol.append(matrix[bottom][i])
                bottom -= 1
            
            # bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    sol.append(matrix[i][left])
                left += 1
        
        return sol
