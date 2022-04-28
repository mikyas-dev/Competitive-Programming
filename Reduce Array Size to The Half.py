class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        di={}
        for i in arr:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        di=sorted(di.items(), key =
             lambda item:item[1])
        di=dict(di)
        col=0
        ans=0
        li=list(di.keys())
        q=len(di)-1
        for j in range(len(di)):
            x=li[q-j]
            col+=di[x]
            ans+=1
            if col>=len(arr)//2:
                break
        return ans
