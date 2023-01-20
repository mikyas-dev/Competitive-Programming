class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans=sorted(Counter(arr).items(), key= lambda x:x[1],reverse=True)
        res=tem=0
        for i in ans:
            tem+=i[1]
            res+=1
            if tem>=len(arr)//2:
                break
        return res
            

            
