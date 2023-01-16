class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        temp = nums.count(target)
        if temp == -1:
            return []
        for i in range(temp):
            ans.append(nums.index(target)+i)
        return ans
