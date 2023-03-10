class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backTracker(temp,nex):
            print(temp)

            ans.append(temp.copy())
            
            for i in range(nex,n):
                temp.append(nums[i])

                backTracker(temp, i+1)

                temp.pop()
        backTracker([],0)
        return ans
