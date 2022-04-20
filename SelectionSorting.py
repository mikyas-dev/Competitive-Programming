class Solution: 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,n-1):
            min = i
            for j in range(i+1,n):
                if arr[j]<arr[min]:
                    min = j
            if min !=i:
                arr[min],arr[i]=arr[i],arr[min]
        
