class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i , c in enumerate(s):
            lastIndex[c] = i
        
        ans = []

        size = end = 0

        for i , c in enumerate(s):
            size += 1
            end = max(end,lastIndex[c])

            if i == end:
                ans.append(size)
                size = 0
            
        return ans

            
        