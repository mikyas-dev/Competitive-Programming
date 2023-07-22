class Solution:
    def firstMissingPositive(self,nums):
        def cyclicSort(newTenantPrevHome, newTenant):
            newHome = newTenant - 1
            if newHome >= len(nums):
                nums[newTenantPrevHome] = 0
                return
            elif nums[newHome] == newTenant:
                if newTenantPrevHome != newHome:
                    nums[newTenantPrevHome] = 0
                return

            nums[newTenantPrevHome] = 0
            if nums[newHome] != 0:
                cyclicSort(newHome, nums[newHome])
            nums[newHome] = newTenant

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i, num in enumerate(nums):
            cyclicSort(i, num)

        for i, num in enumerate(nums):
            if num == 0:
                return i + 1

        return len(nums) + 1
