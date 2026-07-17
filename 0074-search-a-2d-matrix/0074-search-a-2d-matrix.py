class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // n
            col = mid % n

            el = matrix[row][col]

            if target == el:
                return True

            elif target > el:
                l = mid + 1

            else:
                r = mid - 1

        return False