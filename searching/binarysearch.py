"""
1. Binary search works on divide and conquer method.
2. It works only on the sorted array.
"""

def binarySearch(arr, n, x):
    beg = 0
    end = n-1
    mid = (beg+end)//2
    while beg < end and arr[mid] != x:
        if arr[mid] > x:
            end = mid - 1
        else:
            beg = mid +1
        mid = (beg+end)//2
    
    if arr[mid] == x:
        return mid
    else:
        return -1

n = int(input("Enter the number of elements: "))
print("Enter the elements in ascending order.")
arr = []
for i in range(n):
    arr.append(int(input("Enter number: ")))
x = int(input("Element you want to search: "))

print("Entered Array:", arr)
    
search = binarySearch(arr, n, x)
print("Element", x, "is present at index", search)