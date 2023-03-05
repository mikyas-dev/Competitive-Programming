class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans=0

        for i in houses:
            lo, hi = 0, len(heaters)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if heaters[mid] < i: lo = mid + 1
                else: hi = mid
            cur = lo

            if cur<len(heaters):
                if cur!=0 and abs(heaters[cur-1]-i)<heaters[cur]-i:
                    ans=max(ans,abs(heaters[cur-1]-i))
                else:
                    ans=max(ans,heaters[cur]-i)
            else:
                ans=max(ans,abs(heaters[cur-1]-i))

           
        return ans
