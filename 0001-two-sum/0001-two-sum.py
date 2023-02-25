class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference={}
        for i in range(len(nums)):
            differ=target-nums[i]
            if differ in difference:
                return [difference[differ],i]
            difference[nums[i]]=i