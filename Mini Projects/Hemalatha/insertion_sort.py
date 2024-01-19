def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        current_element = arr[i]
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element

# Example usage:
my_list = [14, 3, 25, 12, 22, 11, 30]
insertion_sort(my_list)
print("Sorted array:", my_list)

