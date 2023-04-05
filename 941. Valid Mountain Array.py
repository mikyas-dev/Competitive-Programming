class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        def sort(arr):
            for i in range(1,len(arr)):
                if arr[i-1]>=arr[i]:
                    return False
            return True
        if len(arr) < 3:
            return False
        idx = arr.index(max(arr))
        if idx ==0 or idx == len(arr)-1:
            return False
        
        left = arr[:idx]
        right = arr[-1:idx - len(arr) - 1:-1]
        # print(left,right)

        if sort(left) and sort(right):
            return True
        return False

            


