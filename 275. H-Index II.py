class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low , high = 0 , len(citations)-1
        
        while low <= high:
            mid = (low+high)//2

            if citations[mid] <= len(citations)-1-mid:
                low = mid + 1
            else: high = mid - 1
        return len(citations)-low
