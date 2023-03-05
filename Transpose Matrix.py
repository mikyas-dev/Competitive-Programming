class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for m in range(len(matrix[0])):
            temp=[]
            for n in range(len(matrix)):
                temp.append(matrix[n][m])
            ans.append(temp)
        return ans
