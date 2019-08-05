nums = [1, 3, 2, -7, 5]
val = 7

# Use range() to find two indices that sum to a specific value
def find_indices(nums, val):
    """Given a list, find the two indices that sum to a specific value"""
    for outer in range(len(nums)):
        for inner in range(len(nums)):
            if nums[outer] + nums[inner] == val:
                return (outer, inner)
    return False


# Use enumerate() to two indices that sum to a specific value
def find_indices(nums, val):
    """Given a list, find the two indices that sum to a specific value"""
    for i, outer_num in enumerate(nums):
        for j, inner_num in enumerate(nums):
            if outer_num + inner_num == val:
                return (i, j)
    return False
