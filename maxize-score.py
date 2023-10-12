class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def solve(state, i):
            if i == (len(nums) // 2) + 1:
                return 0
            
            best = 0

            for x in range(len(nums)):
                if (1 << x) & state:
                    continue
                
                for y in range(x + 1, len(nums)):
                    if (1 << y) & state:
                        continue
                    
                    best = max(best, i * gcd(nums[x], nums[y]) + solve((1 << x) | (1 << y) | state, i + 1))

            return best
        
        return solve(0, 1)
