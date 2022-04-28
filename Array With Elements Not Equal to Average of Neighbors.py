class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums)-1,2):
            ans.append(nums[i+1])
            ans.append(nums[i])
        if len(nums)%2:
            ans.append(nums[len(nums)-1])
        return ans
