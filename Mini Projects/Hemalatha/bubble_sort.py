def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [13, 34, 25, 12, 22, 11, 70]
bubble_sort(my_list)
print("Sorted array:", my_list)

