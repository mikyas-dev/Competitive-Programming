class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxima = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i],maxima = maxima, max(arr[i],maxima)
        
        return arr
