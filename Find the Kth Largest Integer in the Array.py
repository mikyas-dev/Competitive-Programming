class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sor(val):
            temp=int(val)
            return temp
        nums.sort(key=sor)
        return nums[len(nums)-k]
