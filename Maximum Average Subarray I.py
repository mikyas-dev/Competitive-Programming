class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=sum(nums[:k])
        ans=total
        l,r=0,k
        while r<len(nums):
            total=total-nums[l]+nums[r]
            ans=max(ans,total)
            l+=1
            r+=1
        return ans/k
