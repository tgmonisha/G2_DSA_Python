#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge = []   
        i = j = 0
        while i < len(left) and j < len(right):
          if left[i] <= right[j]:
              merge.append(left[i])
              i += 1
          else:
              merge.append(right[j])
              j += 1
        while i < len(left):
            merge.append(left[i])
            i += 1

        while j < len(right):
            merge.append(right[j])
            j += 1

         
        for k in range(len(merge)):
            arr[k] = merge[k]

 
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print(my_list)
#selection sort
def selection_sort(arr):
  for i in range(len(arr)-1):
    min=i
    j=i+1
    for j in range(i+1,len(arr)):
      if (arr[min]>arr[j]):
        min=j
    if(i!=min):
      arr[min],arr[i]=arr[i],arr[min]
  return arr
#insertion sort
def insort_sort(arr):
  n=len(arr)
  i=1
  for i in range(n):
    j=i-1
    while(j>=0):
      if(arr[j]>arr[j+1]):
         arr[j],arr[j+1]=arr[j+1],arr[j]
      else:
        break
      j-=1
    i=i+1
#bubbel sort
def bubbel_sort(arr):
  for i in range(len(arr)):
    #already last element was sorted
    for j in range(len(arr)-i-1):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr
