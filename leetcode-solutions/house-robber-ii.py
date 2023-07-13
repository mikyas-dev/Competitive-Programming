class Solution:

    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return max(nums)
        def helper(nums):
            
            nums.append(0)

            for i in range(len(nums)-4,-1,-1):
                nums[i] += max( nums[i+2], nums[i+3])
            
            return max(nums[0],nums[1])
        
        return max(helper(nums[1:]),helper(nums[:-1]))
        