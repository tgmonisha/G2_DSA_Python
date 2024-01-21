def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

data = []
n = int(input("Enter the number of elements: ")

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    data.append(num)

option = int(input("Choose an option:\n1. Linear Search\n2. Binary Search\n3. Bubble Sort\n4. Insertion Sort\n5. Selection Sort\n6. Merge Sort\nEnter the option number: "))

if option == 1:
    target = int(input("Enter the target value: "))
    result = linear_search(data, target)
    if result != -1:
        print(f"Linear Search: {target} found at index {result}")
    else:
        print(f"Linear Search: {target} not found")
elif option == 2:
    data.sort()
    target = int(input("Enter the target value: "))
    result = binary_search(data, target)
    if result != -1:
        print(f"Binary Search: {target} found at index {result}")
    else:
        print(f"Binary Search: {target} not found")
elif option == 3:
    bubble_sort(data)
    print("Bubble Sort:", data)
elif option == 4:
    insertion_sort(data)
    print("Insertion Sort:", data)
elif option == 5:
    selection_sort(data)
    print("Selection Sort:", data)
elif option == 6:
    merge_sort(data)
    print("Merge Sort:", data)
else:
    print("Invalid option")
