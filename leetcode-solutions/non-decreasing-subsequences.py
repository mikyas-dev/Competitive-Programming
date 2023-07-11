class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backTrack(cur,idx):
            flag = False
            if len(cur)>1:
                ans.add(tuple(cur))
            
            if idx == len(nums):
                return

            if not cur or nums[idx]>= cur[-1]:
                flag = True
                cur.append(nums[idx])
            
            backTrack(cur,idx+1)
            
            if flag:
                cur.pop()

            backTrack(cur,idx+1)
        
        backTrack([],0)

        return list(ans)
