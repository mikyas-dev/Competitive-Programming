class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0

        i =0

        while i < len(nums):
            pos = nums[i] - 1
            if nums[pos] == nums[i] and pos != i:
                ans = nums[pos]
                break
            
            nums[pos],nums[i] = nums[i], nums[pos]

            if nums[i]-1 == i:
                i+=1

        
        return ans