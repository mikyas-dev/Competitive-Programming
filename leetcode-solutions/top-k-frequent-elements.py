class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=dict(sorted(Counter(nums).items(),key=lambda x:x[1],reverse=True))
        return list(ans.keys())[:k]