def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
list_item  = [34, 55, 65, 67, 62, 874, 12, 6]
selection_sort(list_item )
print("Sorted array is:", list_item )

