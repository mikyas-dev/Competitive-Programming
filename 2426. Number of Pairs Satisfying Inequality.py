class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i]-nums2[i])
        
        def merge(left, right):
            result = []
            l = r = 0
            while l < len(left) and r < len(right):

                if left[l] < right[r]:
                    result.append(left[l])
                    l+=1
                else:
                    result.append(right[r])
                    r+=1

            while l < len(left):
                result.append(left[l])
                l+=1
            while r < len(right):
                result.append(right[r])
                r+=1

            return result

        def mergeSort(left, right, arr):
            nonlocal ans

            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2

            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            l = r = 0

            while l < len(left_half) and r < len(right_half):

                if left_half[l] - right_half[r]<= diff:
                    ans+=len(right_half)-r
                    l+=1
                else:
                    r+=1



            return merge(left_half, right_half)
        

        mergeSort(0,len(nums)-1,nums)
        
        return ans
                    
