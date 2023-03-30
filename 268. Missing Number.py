class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = len(nums)*(len(nums) + 1)//2

        return tot  - sum(nums)
