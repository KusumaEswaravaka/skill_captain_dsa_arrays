def product_except_self(nums):
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Create left_products and right_products arrays
    left_products = [1] * n
    right_products = [1] * n

    # Step 2: Fill left_products array
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Step 3: Fill right_products array
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Step 4: Construct the answer array
    answer = [left_products[i] * right_products[i] for i in range(n)]

    return answer

# Example usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
