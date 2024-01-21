def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False

        # Last i elements are already in place, so no need to compare them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
my_list = [170, 45, 75, 90, 802, 24, 2, 66]
bubble_sort(my_list)
print("Sorted array is:", my_list)

