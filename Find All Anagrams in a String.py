class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = Counter(p)
        hold = {}
        ans = []
        slow = 0

        for fast in range(len(s)):
            if s[fast] in p:
                while s[fast] in hold and hold[s[fast]] == p[s[fast]]:
                    hold[s[slow]] -= 1
                    slow+=1
                hold[s[fast]] = 1 + hold.get(s[fast],0)
                if hold == p:
                    ans.append(slow)
                    hold[s[slow]] -= 1
                    slow+=1
            else:
                slow = fast + 1
                hold = {}
        
        return ans

        
