class Solution:
    def __init__(self):
        self.memo = dict()

    def rob(self, nums: List[int]) -> int:
        self.ans = 0
        @cache
        def dp(idx , tot):
            if idx >= len(nums):
                self.ans = max(self.ans,tot)
                return 
            
            dp(idx+2,tot+nums[idx])
            dp(idx+1, tot)

        dp(0,0)

        return self.ans