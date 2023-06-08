class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        left = 0
        right = (row * len(matrix)) - 1
        mid = ((left + right)//2) + ((left + right)%2)
        i = mid//row
        j = mid % row
        while(left <= right):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = ((left + right)//2) + ((left + right)%2)
            i = mid//row
            j = mid % row
        return False