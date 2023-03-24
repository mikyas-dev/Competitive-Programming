class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        # def partition(array, low, high):

        #     pivot = array[high]

        #     i = low - 1

        #     for j in range(low, high):
        #         if array[j] <= pivot:
        #             i += 1
        #         else:
        #             continue

        #         array[i], array[j] = array[j], array[i]

        #     array[i + 1], array[high] = array[high], array[i + 1]

        #     return i + 1

        # def quickSort(array, low, high):
        #     if low < high:

        #         pi = partition(array, low, high)
        #         quickSort(array, low, pi - 1)
        #         quickSort(array, pi + 1, high)


        # size = len(nums)

        # quickSort(nums, 0, size - 1)

        # return nums[size - k]

        nums.sort()
        return nums[len(nums)-k]
