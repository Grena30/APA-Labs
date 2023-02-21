def counting_sort(arr):
    # Find the range of values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Count the number of occurrences of each value in the array
    count = [0] * (max_val - min_val + 1)
    for val in arr:
        count[val - min_val] += 1

    # Compute the cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create a sorted array
    sorted_arr = [0] * len(arr)
    for val in reversed(arr):
        sorted_arr[count[val - min_val] - 1] = val
        count[val - min_val] -= 1

    return sorted_arr
