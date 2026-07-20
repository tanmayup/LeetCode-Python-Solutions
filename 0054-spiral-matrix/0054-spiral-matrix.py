class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            if matrix:
                for el in matrix[0]:
                    ans.append(el)
                matrix.pop(0)

            if matrix:
                for i in range(len(matrix)):
                    ans.append(matrix[i][-1])
                    matrix[i].pop(-1)

            matrix = [row for row in matrix if row]

            if matrix:
                for i in range(len(matrix[-1])-1, -1, -1):
                    ans.append(matrix[-1][i])
                matrix.pop(-1)


            if matrix:
                for i in range(1, len(matrix)+1):
                    ans.append(matrix[-i][0])
                    matrix[-i].pop(0)

            matrix = [row for row in matrix if row]

        return ans
