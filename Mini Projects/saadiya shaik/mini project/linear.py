def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not in the list

# Example usage:
my_list = [23, 66, 38, 75, 95, 42, 60]
target_element = 60
result = linear_search(my_list, target_element)

if result != -1:
    print(f'Target element {target_element} found at index {result}')
else:
    print(f'Target element {target_element} not found in the list')

