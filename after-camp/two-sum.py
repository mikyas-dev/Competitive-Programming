class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx in range(len(nums)):
            if target - nums[idx] in hashMap:
                return [hashMap[target - nums[idx]], idx]

            hashMap[nums[idx]] = idx

        return [] 

        