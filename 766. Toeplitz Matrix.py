class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix)-1):
            for j in range(1,len(matrix[i])):
                if matrix[i][j-1] != matrix[i+1][j]:
                    return False
        
        return True
