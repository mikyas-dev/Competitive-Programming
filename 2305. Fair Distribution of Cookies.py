class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        ans = float('inf')
        fair = [0]*k
        def rec(i):
            nonlocal ans

            if i >= len(cookies):
                return max(fair)
                
            if max(fair) >= ans:
                return ans

            for j in range(k):

                fair[j] += cookies[i]
                cur = rec(i+1)
                ans = min(cur,ans)
                fair[j] -= cookies[i]

            return ans
        
        return rec(0)

