class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        col = 0
        while i < n:
            pos = nums[i] - 1
            if pos != i and nums[pos]!=nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
                
            elif pos != i and nums[pos]==nums[i]:
                col = i
                i+=1
            else:
                i += 1
        # print(col,nums)
        return [nums[col],col+1]

    
