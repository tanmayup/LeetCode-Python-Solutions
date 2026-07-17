class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final, matrixc = [], []
        matrixc[:] = matrix[:]
        count = 0
        print(matrix)

        while len(matrix) != 1:
            for i in range(len(matrix[0])):
                final.append(matrix[0][i])

            matrix = []
            matrixc.pop(0)

            for j in range(1, len(matrixc[0]) + 1):
                newrow = []
                for i in range(len(matrixc)):
                    newrow.append(matrixc[i][(-1) * j])
                matrix.append(newrow)

            matrixc[:] = matrix[:]

        for el in matrix[0]:
            final.append(el)

        return final