class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
            n = len(matrix)-1
            for i in range(0, ceil(n/2)):
                for j in range(i,n-i):
                    matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] = matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]