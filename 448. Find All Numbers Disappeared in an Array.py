class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sol = set()
        for i in range(len(nums)):
            sol.add(i+1)

        for i in nums:
            if i in sol:
                sol.remove(i)
        
        return list(sol)


