#practical 4 daa
#Binary search
def binary_search(array , n):
    low = 0
    high = len(array) -1
    
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == n:
            return mid
        elif array[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [3,4,5,6,7,8,9]
n = 5

result = binary_search(array, n)

if result != -1:
    print("Element is present at index",result)
else:
    print("Element not found")
