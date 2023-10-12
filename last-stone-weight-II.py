class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_stones = sum(stones)
        target = ceil(total_stones / 2)
        memo = {}

        def dp(idx, tot):
            if idx == len(stones) or tot >= target: 
                return abs(tot - (total_stones - tot))
            
            if (idx,tot) in memo:
                return memo[(idx,tot)]
            

            memo[(idx,tot)] = min(dp(idx + 1 , tot), dp(idx+1, tot + stones[idx]))
            return memo[(idx,tot)]

        return dp(0,0)

