a = [65, 35, 22, 17, 16]
for i in range(len(a)):
    min = i
    for j in range(i+1, len(a)):
        if a[min] > a[j]:
            min = j 
    a[i], a[min] = a[min], a[i]
print ("Sorted array")
for i in range(len(a)):
    print("%d" %a[i],end=" , ") 
