def bucket_sort(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    n = len(arr)

    # Calculate the range and the size of each bucket
    bucket_range = (max_val - min_val) / (n - 1)

    # Create empty buckets
    buckets = [[] for _ in range(n)]

    # Put elements into their respective buckets
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # Sort elements within each bucket using insertion sort
    for i in range(n):
        insertion_sort(buckets[i])

    # Concatenate sorted elements from each bucket
    k = 0
    for i in range(n):
        for num in buckets[i]:
            arr[k] = num
            k += 1

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

# Example usage
arr = [0.42, 0.32, 0.91, 0.01, 0.72, 0.63, 0.35]
print("Unsorted array:", arr)
bucket_sort(arr)
print("Sorted array:", arr)