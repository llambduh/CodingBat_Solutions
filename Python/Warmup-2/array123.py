def array123(nums):
    """
    Check if the consecutive sequence 1, 2, 3 appears anywhere in the array.
    
    Args:
        nums: A list of integers to search through
        
    Returns:
        True if the sequence [1, 2, 3] is found consecutively, False otherwise
    """
    
    # Loop through the array, stopping 2 positions before the end
    # We use len(nums)-2 because we need to check 3 consecutive elements (i, i+1, i+2)
    # This prevents an IndexError when accessing nums[i+2]
    # For example, if len(nums) = 5, we check indices 0, 1, 2 (stopping before 3)
    for i in range(len(nums)-2):
        
        # Check if the current position and the next two positions
        # contain the sequence 1, 2, 3 in that exact order
        # nums[i] checks the current element
        # nums[i+1] checks the next element
        # nums[i+2] checks the element after that
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            # If we find the sequence, immediately return True
            # No need to continue searching once we've found it
            return True
    
    # If we've checked all possible consecutive triplets and haven't found [1, 2, 3],
    # return False
    # This line only executes if the for loop completes without finding the sequence
    return False
