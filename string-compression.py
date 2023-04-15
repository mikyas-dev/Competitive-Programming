class Solution:
    def compress(self, chars: List[str]) -> int:
        slow=0
        counter=0
        for fast in range(len(chars)):
            if chars[slow]!=chars[fast]:
                chars[counter]=chars[slow]
                counter+=1
                if fast-slow>1:
                    nums=list(str(fast-slow))
                    for k in nums:
                        chars[counter]=k
                        counter+=1
                slow=fast
        chars[counter]=chars[slow]
        counter+=1
        if fast-slow+1>1:
            nums=list(str(fast-slow+1))
            for k in nums:
                chars[counter]=k
                counter+=1
        return counter