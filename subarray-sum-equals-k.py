class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sub = defaultdict(int)

        sub[0]+=1
        tot = 0

        for i in range(len(nums)):
            if tot + nums[i] - k in sub:
                ans+=sub[tot + nums[i] - k]

            tot += nums[i]
            sub[tot] += 1
        return ans