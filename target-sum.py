class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dp(idx , tot):
            if idx == len(nums):
                if tot == 0:
                    return 1
                return 0
            ways = (idx,tot)
            if ways not in memo:
    
                memo[ways] = dp(idx+1,tot-nums[idx])+dp(idx+1,tot+nums[idx])

            return memo[ways]
        
        return dp(0 , target)