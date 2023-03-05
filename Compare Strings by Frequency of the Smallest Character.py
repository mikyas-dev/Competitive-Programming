class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q=[]
        w=[]
        res=[]

        for valq in queries:
            temp = list(valq)
            temp.sort()
            q.append((Counter(temp))[temp[0]])
        for valw in words:      
            temp = list(valw)
            temp.sort()
            w.append((Counter(temp))[temp[0]])

        w.sort()
        for val in q:
            low , high = 0 , len(w)
            ans = 0

            while low < high:
                mid = (low+high)//2
                
                if w[mid] > val:high = mid 
                else:low = mid + 1
            ans = low-1
                
            res.append(len(w)-1-ans)

        return res
