class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backTracker(temp,idx):
            if temp not in ans:
                ans.append(temp.copy())
        
            if idx == n:
                return 
            
            
            temp.append(nums[idx])
            backTracker(temp, idx+1)

            temp.pop()
            backTracker(temp,idx+1)

        backTracker([],0)
        return ans