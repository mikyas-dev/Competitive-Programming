class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            j=i-1
            temp = nums[i]
            while nums[j]>temp and j>=0:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=temp
