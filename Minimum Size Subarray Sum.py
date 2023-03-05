class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        sum = 0
        slow = 0
        for fast in range(len(nums)):
            sum += nums[fast]
            
            while sum >= target:
                ans = min(ans, fast - slow +1)
                sum-=nums[slow]
                slow+=1

        return 0 if ans==len(nums)+1 else ans
        
