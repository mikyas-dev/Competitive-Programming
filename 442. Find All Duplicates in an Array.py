class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if pos != i and nums[pos]!=nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        
        for idx,val in enumerate(nums):
            if idx+1 != val:
                ans.append(nums[idx])

        return ans


