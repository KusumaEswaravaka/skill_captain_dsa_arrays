arr = [1,2,3,4,5,6,7]

def find_max_min(arr, low, high):
    # If the array contains only one element
    if low == high:
        return arr[low], arr[low]

    # If the array contains only two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array into two halves
    mid = (low + high) // 2
    max1, min1 = find_max_min(arr, low, mid)
    max2, min2 = find_max_min(arr, mid + 1, high)

    # Combine the results
    return max(max1, max2), min(min1, min2)

# Example usage
if __name__ == "__main__":
    
    
    if not arr:
        print("Array should not be empty.")
    else:
        max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
        print("Maximum value:", max_val)
        print("Minimum value:", min_val)
