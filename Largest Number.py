
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num==0 for num in nums):
            st="0"
        else:
            for i in range(0,len(nums)-1):
                min=i
                for j in range(i+1,len(nums)):
                    if int(str(nums[min])+str(nums[j]))<int(str(nums[j])+str(nums[min])):
                        min=j
                if min !=i:
                    nums[min],nums[i]=nums[i],nums[min]

            st="".join(map(str,nums))
        return st
