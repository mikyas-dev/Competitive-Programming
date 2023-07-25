def count_elements_less_than(arr1, arr2):
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    result = []
    for element in arr2:
        count = binary_search(arr1, element)
        result.append(count)

    return result

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

output = count_elements_less_than(arr1, arr2)
print(*output)
