class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        ans=0
        while i<j:
            if ans < nums[i]+nums[j]:
                ans = nums[i]+nums[j]
            i,j=i+1,j-1
        return ans
