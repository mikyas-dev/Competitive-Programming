class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        a=[]
        for i in arr:
            a.append(i)
        a.sort()
        ans=[]
        if a==arr:
            return []
        for j in range(len(arr)):
            if j==0:
                k=a.index(a[0])
                ans.append(k+1)
                m,n=0,k
                while m<n:
                    arr[m],arr[n]=arr[n],arr[n]
                    m+=1
                    n-=1
            c,v=0,arr.index(a[-1-j])
            ans.append(v+1)
            while c<v:
                arr[c],arr[v]=arr[v],arr[c]
                c+=1
                v-=1
            c,v=0,len(arr)-1-j
            ans.append(v+1)
            while c<v:
                arr[c],arr[v]=arr[v],arr[c]
                c+=1
                v-=1
            if arr==a:
                break
        return ans
                    
        
