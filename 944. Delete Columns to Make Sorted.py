class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            a = strs[0][i]
            for s in strs:
                if a > s[i]:
                    count += 1
                    break
                else:
                    a = s[i]
        return count
            
