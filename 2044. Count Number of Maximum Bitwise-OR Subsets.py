class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        
        def backTracker(temp,nex,orVal):

            ans.append((orVal,temp.copy()))
            
            for i in range(nex,n):
                temp.append(nums[i])

                backTracker(temp, i+1,orVal | nums[i])

                temp.pop()
        backTracker([],0,0)
        ans.sort(reverse = True)
        for i in range(1,len(ans)):
            if ans[i][0] != ans[i-1][0]:
                break
        return i

