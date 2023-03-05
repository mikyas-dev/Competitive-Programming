class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = Counter(s1)
        hold = {}
        slow = 0

        for fast in range(len(s2)):
            if s2[fast] in p:
                while s2[fast] in hold and hold[s2[fast]] == p[s2[fast]]:
                    hold[s2[slow]] -= 1
                    slow+=1
                hold[s2[fast]] = 1 + hold.get(s2[fast],0)
                if hold == p:
                    return True
            else:
                slow = fast + 1
                hold = {}
        
        return False
