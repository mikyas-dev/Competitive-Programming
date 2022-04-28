class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out=[]
        n=len(nums)
        for i in range(0,n-1):
            min=i
            for j in range(i+1,n):
                if nums[j]<nums[min]:
                    min = j
            if min !=i:
                nums[min],nums[i]=nums[i],nums[min]
        for k in range(n):
            if target == nums[k]:
                out.append(k)
        return out
        
