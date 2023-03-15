"""
Linear Search searches an item in the list by traversing the whole array
and comparing with every item.
if Item is present in the array then we return the index else return -1.
"""

def linearSearch(array, n, x):
    for index in range(n):
        if array[index] == x:
            return index
    return -1

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter number: ")))
x = int(input("Element you want to search: "))

print("Entered Array:")
for i in range(n):
    print(arr[i], end=' ')
print()
    
search = linearSearch(arr, n, x)
if(search != -1):
    print(f"The item is present in the array at index {search}.")
else:
    print("The item is not present in the array.")