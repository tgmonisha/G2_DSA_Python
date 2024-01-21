def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted into the sorted part
        j = i - 1  # Index of the last element in the sorted part

        # Move elements of the sorted part that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [170, 45, 75, 90, 802, 24, 2, 66]
insertion_sort(my_list)
print("Sorted array is:", my_list)

