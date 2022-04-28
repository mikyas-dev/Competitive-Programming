class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            art=nums[l[i]:r[i]+1]
            art.sort()
            m,n=0,1
            k=art[m]-art[n]
            while m<n and n<len(art):
                if art[m]-art[n]==k:
                    m+=1
                    n+=1
                else:
                    break
            if n==len(art):
                ans.append(True)
            else:
                ans.append(False)
        return ans
