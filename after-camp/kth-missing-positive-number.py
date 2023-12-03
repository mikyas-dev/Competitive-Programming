class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        for i in range(1,k+arr[-1]+1):
            if i not in set(arr):
                k-=1
            if k==0:
                ans = i
                break
        return ans