def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        # If the element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If the element is smaller than the middle element, search the left subarray
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        # Else the element is in the right subarray
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1  # Element is not present in the array

if __name__ == "__main__":
    # Test array (must be sorted)
    arr = [2, 3, 4, 10, 40, 50, 60]
    target_element = 10

    # Function call
    result = binary_search(arr, 0, len(arr) - 1, target_element)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in the array")
