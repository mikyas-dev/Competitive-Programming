class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        numsCopy = nums.copy()
        numsCopy.sort()
        for i in nums:
            ans.append(numsCopy.index(i))
        return ans
