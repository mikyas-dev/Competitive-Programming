class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        ans=[]
        for m in range(len(nums)//2):
            ans.append(nums[i]+nums[j])
            i+=1
            j-=1
        return max(ans)
