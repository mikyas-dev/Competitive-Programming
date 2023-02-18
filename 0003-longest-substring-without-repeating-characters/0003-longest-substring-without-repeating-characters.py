class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast,slow=0,0
        ans=0
        checker=set()
        while fast<len(s):
            while s[fast] in checker:
                checker.remove(s[slow])
                slow+=1
            else:
                checker.add(s[fast])
            ans=max(ans,fast-slow+1)
            fast+=1
        return ans

            