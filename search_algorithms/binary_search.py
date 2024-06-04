def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    example_array = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search(example_array, x)
    print("Element is present at index:", result if result != -1 else "Element is not present in array")
