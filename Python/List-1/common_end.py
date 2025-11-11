def common_end(a, b):
    """
    Determines if two arrays share a common first or last element.
    
    This function compares the first elements and last elements of two arrays
    to check if either pair matches. It returns True if at least one pair matches,
    False otherwise.
    
    Parameters:
    -----------
    a : list
        The first array of integers (guaranteed to have at least 1 element)
    b : list
        The second array of integers (guaranteed to have at least 1 element)
    
    Returns:
    --------
    bool
        True if the arrays have the same first element OR the same last element
        False if neither the first nor last elements match
    
    Examples:
    ---------
    common_end([1, 2, 3], [7, 3]) → True (last elements match: 3 == 3)
    common_end([1, 2, 3], [7, 3, 2]) → False (1 != 7 and 3 != 2)
    common_end([1, 2, 3], [1, 3]) → True (first elements match: 1 == 1)
    """
    
    # Compare first elements using index [0] and last elements using index [-1]
    # The 'or' operator means we return True if EITHER condition is True
    
    # a[0] == b[0]: Checks if the first element of array a equals the first element of array b
    # a[-1] == b[-1]: Checks if the last element of array a equals the last element of array b
    # Using negative indexing [-1] is a Python feature that accesses the last element
    
    return a[0] == b[0] or a[-1] == b[-1]
    
    # Note: This solution is efficient (O(1) time complexity) because it only 
    # accesses specific indices rather than iterating through the entire arrays
    