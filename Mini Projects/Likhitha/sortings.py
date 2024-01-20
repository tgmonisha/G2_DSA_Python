#LINEAR SEARCH IMPLEMENTATION IN PYTHON

def linear_search(arr,key):
	for i in range(len(arr)):
		if(arr[i]==key):
			return i
	return -1
arr=[4,6,3,2,7]
key=int(input("enter key value: "))
res=linear_search(arr,key)
if(res==-1):
	print("element not found")
else:
	print("element found at index:",res)
	
	


#BINARY SEARCH IMPLEMENTATION IN PYTHON
def binarySearch(array, x, low, high):
	# Repeat until the pointers low and high meet each other
	while low <= high:
		mid = low + (high - low)//2
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			low = mid + 1
		else:
			high = mid - 1
	return -1
array = [9,5,7,3,2,1,8]
x = 8
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
	print("Element is present at index " + str(result))
else:
    print("Not found")	
	
	
	
	
#BUCKET SORT IN PYTHON


def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.43, .31, .23, .52, .32, .48, .51]
print("Sorted Array is:",bucketSort(array))
	
	
	





#RADIX SORT IN PYTHON

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
data = [12,44,5,23,1,67,100]
radixSort(data)
print("sorted data is: ",data)	











	

#HEAP SORT IN PYTHON

def heapify(arr, n, i):
	# Find largest among root and children
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
  
	if l < n and arr[i] < arr[l]:
  		largest = l
  
	if r < n and arr[largest] < arr[r]:
   		largest = r
  
   	# If root is not largest, swap with largest and continue heapifying
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
def heapSort(arr):
	n = len(arr)
  	# Build max heap
	for i in range(n//2, -1, -1):
   		heapify(arr, n, i)
  
	for i in range(n-1, 0, -1):
    	# Swap
	    arr[i], arr[0] = arr[0], arr[i]
	    #heapify root element
	    heapify(arr,i,0)
  
arr = [56,46,32,11,89,54]
heapSort(arr)
print("Sorted array is",arr)

	
#SAMPLE OUTPUT FOR ALL ABOVE PROGRAMS	
"""enter key value: 4
element found at index: 0
Element is present at index 6
Sorted Array is: [0.23, 0.31, 0.32, 0.43, 0.48, 0.51, 0.52]
sorted data is:  [1, 5, 12, 23, 44, 67, 100]
Sorted array is [11, 32, 46, 54, 56, 89]"""
	


