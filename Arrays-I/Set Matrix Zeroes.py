class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    if (j != 0):
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if (matrix[0][0] == 0):
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0

        if (col0 == 0):
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
