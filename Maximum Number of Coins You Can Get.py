class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n=len(piles)//3
        ans=0
        for i in range(n):
            c=2*i+1
            ans+=piles[c]
        return ans
