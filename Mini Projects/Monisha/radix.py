def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1

    # Perform counting sort for every digit position
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# Example usage:
my_list = [70, 55, 85, 60, 72, 44, 22, 96]
radix_sort(my_list)
print("Sorted array is:", my_list)

