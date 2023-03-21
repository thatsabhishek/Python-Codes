def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergesort(left_arr)
        mergesort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr
 
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array:", arr)

mergesort(arr)

print("Sorted Array:", arr)