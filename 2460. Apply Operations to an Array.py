class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        zero = 0
        for idx in range(len(nums)):
            if nums[zero] == 0 and nums[idx] != 0:
                nums[zero], nums[idx] = nums[idx],nums[zero]
            while nums[zero]!=0 and zero < idx:
                zero+=1
        
        return nums
