#BUBBLE SORT IN PYTHON

# Creating a bubble sort function  
def bubble_sort(list1):  
	for i in range(0,len(list1)-1):  
		for j in range(len(list1)-1):  
			if(list1[j]>list1[j+1]):  
				temp = list1[j]  
				list1[j] = list1[j+1]  
				list1[j+1] = temp  
	return list1  
list1 = [89,56,34,2,1,8]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  





#INSERTION SORT IN PYTHON

    # creating a function for insertion  
def insertion_sort(list1):  
# Outer loop to traverse through 1 to len(list1)  
	for i in range(1, len(list1)):  
		value = list1[i]  
		j = i - 1  
		while j >= 0 and value < list1[j]:  
			list1[j + 1] = list1[j]  
			j -= 1 
		list1[j + 1] = value  
	return list1  
list1 = [23,54,1,78,56,44]  
print("The unsorted list is:", list1)  
print("The sorted list1 is:", insertion_sort(list1))               
      
   
   
   
#SELECTION SORT IN PYTHON

def selection_sort(array):  
	length = len(array)  
	for i in range(length-1):  
		minIndex = i  
		for j in range(i+1, length):  
			if array[j]<array[minIndex]:  
				minIndex = j  
		array[i], array[minIndex] = array[minIndex], array[i]  
	return array      
array = [21,6,9,33,3]  
print("THe unsorted list is:" ,array)
print("The sorted array is: ", selection_sort(array))   
 
 
 
 
 
#MERGE SORT IN PYTHON


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:

		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ",arr)
mergeSort(arr, 0, n-1)
print("Sorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")


#QUICK SORT IN PYTHON

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)
data = [6,56,78,33,2,1]
print("\nUnsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
 
 
 
 
#OUTPUT FOR ABOVE PROGRAMS 
"""The unsorted list is:  [89, 56, 34, 2, 1, 8]
The sorted list is:  [1, 2, 8, 34, 56, 89]
The unsorted list is: [23, 54, 1, 78, 56, 44]
The sorted list1 is: [1, 23, 44, 54, 56, 78]
THe unsorted list is: [21, 6, 9, 33, 3]
The sorted array is:  [3, 6, 9, 21, 33]
Given array is:  [12, 11, 13, 5, 6, 7]
Sorted array is
5 6 7 11 12 13 
Unsorted Array
[6, 56, 78, 33, 2, 1]
Sorted Array in Ascending Order:
[1, 2, 6, 33, 56, 78]
"""
