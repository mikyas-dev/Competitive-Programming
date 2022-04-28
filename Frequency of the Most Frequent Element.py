class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=total=ans=0
        for j in range(len(nums)):
            total+=nums[j]
            while nums[j]*(j-i+1)>+total+k:
                total-=nums[i]
                i+=1
            ans=max(ans,j-i+1)
        return ans
