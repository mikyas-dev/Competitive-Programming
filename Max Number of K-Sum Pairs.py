class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i]+nums[j] == k:
                i+=1
                j-=1
                count+=1
                continue
            elif nums[i]+nums[j]<k:
                i+=1
                continue
            elif nums[i]+nums[j]>k:
                j-=1
                continue
        return count
