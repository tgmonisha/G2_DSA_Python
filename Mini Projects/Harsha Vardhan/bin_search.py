def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


arr = [
    int(x)
    for x in input("Enter a sorted array of integers, separated by spaces: ").split()
]
target = int(input("Enter the target element to search for: "))
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
