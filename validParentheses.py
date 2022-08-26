class Solution:
    def isValid(self, s: str) -> bool:
        lis=[s[0]]
        boo=False
        i,j=1,0
        while i<len(s):
            if not lis:
                lis.append(s[i])
                i+=1
                j=0
                continue
            elif (lis[j]=="(" and s[i]==")") or (lis[j]=="{" and s[i]=="}") or (lis[j]=="[" and s[i]=="]"):
                boo=True
                lis.pop()
                j-=1
            else:
                j+=1
                lis.append(s[i])
                boo=False
            i+=1
        return boo and not lis
                
        
