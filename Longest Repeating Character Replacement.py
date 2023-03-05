class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        ans = left = 0

        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right],0)
            maxcount = max(counter.values())

            while (right - left + 1) - maxcount > k:
                counter[s[left]]-=1
                left+=1
            ans = max(ans,right - left + 1)

        return ans
        
       
