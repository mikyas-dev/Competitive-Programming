class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low , high = 1 , max(nums)
        ans = threshold+1

        while low <= high:
            mid = (low+high)//2
            sum = 0

            for i in nums:
                sum+=ceil(i/mid)

            if sum>threshold:
                low = mid+1
            else: high = mid - 1

        return low

