class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        tot = 0
        ans = 0
        for val in nums:
            tot += val
            m = tot%k
            ans += prefix[m]
            prefix[m]+=1
        return ans