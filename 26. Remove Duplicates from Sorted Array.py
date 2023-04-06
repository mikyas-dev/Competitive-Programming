class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for val in nums:
            if ans[-1] != val:
                ans.append(val)
        return len(ans)
                
