class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in set(nums):
            return [bisect_left(nums,target),bisect_right(nums,target)-1]
        else:
            return [-1,-1]
