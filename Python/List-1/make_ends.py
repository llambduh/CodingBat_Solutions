def make_ends(nums):
    """
    Create a new array containing only the first and last elements from the input array.
    
    Parameters:
    -----------
    nums : list of int
        An array of integers with length >= 1
    
    Returns:
    --------
    list of int
        A new array of length 2 containing [first_element, last_element]
    
    Examples:
    ---------
    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]
    """
    
    # Return a new list containing two elements:
    # - nums[0]: The first element (at index 0)
    # - nums[-1]: The last element (negative indexing, -1 refers to the last item)
    #
    # Note: This works even when the array has only 1 element, because:
    # nums[0] and nums[-1] will both refer to the same element,
    # so it returns [element, element]
    #
    # Example: make_ends([5]) → [5, 5]
    
    return [nums[0], nums[-1]]
    