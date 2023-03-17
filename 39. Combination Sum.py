class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(temp, tot,idx):
            if tot == target:
                ans.append(temp.copy())
                return
                
            if idx == len(candidates) or( target - tot )< candidates[idx]:
                return

            

            temp.append(candidates[idx])
            dfs(temp,tot+candidates[idx],idx)

            temp.pop()
            dfs(temp,tot,idx+1)
            

        dfs([],0,0)
        return ans
