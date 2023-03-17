def insertionsort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while temp < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
                
            
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array:", arr)

insertionsort(arr, n)

print("Sorted Array:", arr)