class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0

        def hourChecker(k:int):
            total=0
            for pile in piles:
                total+=ceil((pile)/k)
            return total<=h

        while low<=high:
            mid = (low+high)//2
            if hourChecker(mid):
                ans=mid
                high=mid-1
            elif not hourChecker(mid):
                low=mid+1
        return ans

        
