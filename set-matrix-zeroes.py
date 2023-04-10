class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowflag = set()
        colflag = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rowflag.add(i)
                    colflag.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rowflag or j in colflag:
                    matrix[i][j] = 0