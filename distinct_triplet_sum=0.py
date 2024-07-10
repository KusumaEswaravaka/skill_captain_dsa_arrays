def threeSum(nums):
    # Step 1: Sort the array
    nums.sort()
    result = []
    
    # Step 2: Iterate through the array, using 'i' to fix the first element of the triplet
    for i in range(len(nums) - 2):
        # Skip duplicate elements to avoid duplicate triplets in the result
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Step 3: Use two pointers to find the remaining two elements that sum up to -nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element of the triplet
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element of the triplet
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers inward after finding a valid triplet
                left += 1
                right -= 1
            elif total < 0:
                # If the sum is less than 0, move the left pointer to the right to increase the sum
                left += 1
            else:
                # If the sum is greater than 0, move the right pointer to the left to decrease the sum
                right -= 1
                
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums)) 
