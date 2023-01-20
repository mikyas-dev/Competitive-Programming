class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            num = nums[l[i]:r[i]+1]
            num.sort()
            ans=[]
            for i in range(len(num)-1):
                ans.append(num[i+1]-num[i])
            res.append(max(ans)==min(ans))
        return res
