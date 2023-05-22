def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    n = len(arr)

    # Create a count array to store the count of each element
    count = [0] * (max_val + 1)

    # Store the count of each element in the count array
    for num in arr:
        count[num] += 1

    # Modify the count array to store the actual position of each element
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Create a sorted array to store the sorted elements
    sorted_arr = [0] * n

    # Build the sorted array
    for num in arr:
        index = count[num] - 1
        sorted_arr[index] = num
        count[num] -= 1

    # Copy the sorted array back to the original array
    for i in range(n):
        arr[i] = sorted_arr[i]

# Enter user inputs in an array
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array:", arr)
counting_sort(arr)
print("Sorted array:", arr)
