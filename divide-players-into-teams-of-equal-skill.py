class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()

        i,j = 0, len(skill)-1
        tot = skill[i] + skill[j]
        while i<j:
            if skill[i] + skill[j] != tot:
                return -1
            ans += (skill[i] * skill[j])
            i+=1
            j-=1
        
        return ans