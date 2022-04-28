class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        nums.sort()
        for i in nums:
            if not i in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        lis=dic.values()
        ans=0
        for i in lis:
            if i>1:
                for j in range(i):
                    ans+=j
        return ans
