class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left = 0
        row_right = len(matrix) - 1
        col_left = 0
        col_right = len(matrix[0]) - 1
        row = None

        while row_left <= row_right:
            row_middle = (row_left + row_right) // 2
            if target >= matrix[row_middle][0] and target <= matrix[row_middle][-1]:
                row = row_middle
                break
            elif target < matrix[row_middle][0]:
                row_right = row_middle - 1
            else:
                row_left = row_middle + 1

        if row is not None:
            while col_left <= col_right:
                col_middle = (col_left + col_right) // 2
                if target == matrix[row][col_middle]:
                    return True
                elif target < matrix[row][col_middle]:
                    col_right = col_middle - 1
                else:
                    col_left = col_middle + 1

        return False