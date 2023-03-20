def quick(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while start < end:
        while arr[start] <= pivot and start < ub:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end

def quicksort(arr, lb, ub):
    if lb < ub:
        part = quick(arr, lb, ub)
        quicksort(arr, lb, part-1)
        quicksort(arr, part+1, ub)


n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array:", arr)
    
quicksort(arr, 0, n-1)

print("Sorted Array:", arr)