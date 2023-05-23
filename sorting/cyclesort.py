def cycle_sort(arr):
    n = len(arr)

    # Traverse through each element in the array
    for cycleStart in range(n - 1):
        item = arr[cycleStart]

        # Find the position to put the item
        pos = cycleStart
        for i in range(cycleStart + 1, n):
            if arr[i] < item:
                pos += 1

        # If the item is already in the correct position, skip it
        if pos == cycleStart:
            continue

        # Otherwise, put the item in the correct position
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]

        # Rotate the remaining elements
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

# Enter user inputs in an array
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)
print()

print("Unsorted Array:", arr)
cycle_sort(arr)
print("Sorted array:", arr)
