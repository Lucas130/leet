class Solution:
    def findNumberIn2DArray(self, matrix, target):
        rows_max = len(matrix)
        if rows_max <= 0:
            return False
        cols_max = len(matrix[0])
        for rows in range(0, rows_max):
            for cols in range(cols_max - 1, -1, -1):
                if matrix[rows][cols] == target:
                    return True
                elif matrix[rows][cols] > target:
                    continue
                else:
                    break
        return False

if __name__ == '__main__':
    s = Solution()
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    # matrix = [[-5]]
    # matrix = [[1, 1]]

    print(s.findNumberIn2DArray(matrix, 5))
    print(s.findNumberIn2DArray(matrix, 20))
