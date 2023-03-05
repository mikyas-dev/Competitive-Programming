class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = ans = 0
        store = set()

        for fast in range(len(s)):

            while s[fast] in store:
                store.remove(s[slow])
                slow += 1
            
            store.add(s[fast])
            ans = max(ans,len(store))
            
        return ans

            
