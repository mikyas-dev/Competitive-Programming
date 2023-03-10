class Solution:
    def splitString(self, s: str) -> bool:

        def rec(index,prevVal):

            if index==len(s):
                return True

            for j in range(index,len(s)):
                val=int(s[index:j+1])

                if prevVal-val==1 and rec(j+1,val):
                    return True

            return False

        for i in range(len(s)-1):
            val=int(s[:i+1])

            if rec(i+1,val):
                return True
                
        return False
