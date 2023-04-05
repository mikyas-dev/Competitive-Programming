class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        if row*col != r*c:
            return mat
        
        R = C = 0
        ans = [[0 for _ in range(c)] for _ in range(r)]
        # print(ans)
        for i in range(row):
    
            for j in range(col):
                if C == c:
                    C = 0
                    R += 1
                ans[R][C] = mat[i][j]
                C +=1
                # print(ans)
        
        return ans
                
