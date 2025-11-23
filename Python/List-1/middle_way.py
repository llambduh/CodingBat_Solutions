def middle_way(a, b):
    """
    Extract and return the middle elements from two arrays.
    
    This function takes two integer arrays of length 3 and creates a new array
    containing the middle element (index 1) from each input array.
    
    Parameters:
    -----------
    a : list of int
        First array of exactly 3 integers
    b : list of int
        Second array of exactly 3 integers
    
    Returns:
    --------
    list of int
        A new array of length 2 containing [middle of a, middle of b]
    
    Examples:
    ---------
    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    
    >>> middle_way([7, 7, 7], [3, 8, 0])
    [7, 8]
    
    >>> middle_way([5, 2, 9], [1, 4, 5])
    [2, 4]
    
    Notes:
    ------
    - Assumes both input arrays are exactly length 3
    - The middle element of a length-3 array is at index 1 (0-indexed)
    - No validation is performed on input array lengths
    """
    
    # Access the middle element (index 1) from both arrays
    # and return them together in a new list
    # Index 1 represents the second element, which is the middle of a 3-element array
    return [a[1], b[1]]
    