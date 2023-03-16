
def bubblesort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array:", arr)

bubblesort(arr, n)

print("Sorted Array:", arr)