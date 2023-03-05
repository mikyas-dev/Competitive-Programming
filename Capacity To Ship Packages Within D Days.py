class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights) , sum(weights)
        ans = high+1

        while low <= high:
            sums = mid = (low+high)//2
            count = 1
    
            for val in weights:
                if sums - val < 0:
                    count+=1
                    sums = mid
                sums -= val
                
            if count <= days:
                ans = min(ans,mid)
                high = mid - 1
            else :
                low = mid +1
            
        return ans
