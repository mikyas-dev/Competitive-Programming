class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        
        

        def backTracker(temp,k,nex):
            if len(temp)== k:
                ans.append(temp.copy())
            else:
                for i in range(nex,n+1):
                    temp.append(i)

                    backTracker(temp,k , i+1)

                    temp.pop()
            print(temp, end=" ")
        backTracker(temp,k,1)
        return ans

