# FACTORIAL OF A NUMBER USING RECURSION

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)
num = 5
# check if the number is negative
if(num < 0):
   print("factorial does not exist for negative numbers")
elif(num == 0):
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", fact(num))





# PYTHON PROGRAM TO DISPLAY FIBONACCI SEQUENCE

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))
nterms = 9
# check if the number of terms is valid
if(nterms <= 0):
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fib(i))




# PYTHON PROGRAM FOR RECURSIVE BINARY SEARCH

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can be present in left subarray
   
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 10,20,30,40,50]
search = 30
# Function call
result = binary_search(arr, 0, len(arr)-1, search)
 
if result != -1:
    print("Element 30 is present at index", str(result))
else:
    print("Element is not present in array")

