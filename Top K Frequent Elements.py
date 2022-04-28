class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        di=sorted(di.items(), key =
             lambda item:item[1])
        di=dict(di)
        print(di)
        li=list(di.keys())
        print(li)
        ans=[]
        for i in range(k):
            ans.append(li[-1-i])
        return ans
