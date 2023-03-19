def selectionsort(arr, n):
    for i in range(n):
        small = arr[i]
        loc = i
        for j in range(i+1, n):
            if arr[j] < small:
                small = arr[j]
                loc = j
            arr[i], arr[loc] = arr[loc], arr[i]

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array: ", arr)
    
selectionsort(arr, n)

print("Sorted Array: ", arr)
