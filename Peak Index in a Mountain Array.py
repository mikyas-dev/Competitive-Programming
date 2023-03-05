class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low , high = 0 , len(arr)-1

        while low+1<high:
            mid = (low+high)//2
            if mid!=0 and( arr[mid]>arr[mid-1]):
                low = mid
            else: high = mid
        return low
