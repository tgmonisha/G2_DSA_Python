def bucket_sort(arr):
    # Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)

    # Calculate the range and determine the size of each bucket
    range_val = max_val - min_val
    bucket_size = range_val / len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_size)
        bucket[index].append(num)

    # Sort each bucket individually (you can use any sorting algorithm)
    for i in range(len(arr)):
        bucket[i] = insertion_sort(bucket[i])

    # Concatenate the sorted buckets to get the final sorted array
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

# Example usage:
my_list = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_list = bucket_sort(my_list)
print("Sorted array is:", sorted_list)

