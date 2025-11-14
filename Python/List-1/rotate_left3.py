def rotate_left3(nums):
    """
    Rotates an array of 3 integers one position to the left.
    
    A left rotation moves each element one position to the left, with the 
    first element wrapping around to become the last element.
    
    Parameters:
    -----------
    nums : list
        A list containing exactly 3 integers
        
    Returns:
    --------
    list
        A new list with elements rotated left by one position:
        - Element at index 1 moves to index 0
        - Element at index 2 moves to index 1
        - Element at index 0 moves to index 2
        
    Examples:
    ---------
    >>> rotate_left3([1, 2, 3])
    [2, 3, 1]
    
    >>> rotate_left3([5, 11, 9])
    [11, 9, 5]
    
    >>> rotate_left3([7, 0, 0])
    [0, 0, 7]
    
    How it works:
    -------------
    Instead of modifying the original array, this function creates a new list
    by accessing elements in rotated order:
    - nums[1] becomes the first element (what was second)
    - nums[2] becomes the second element (what was third)
    - nums[0] becomes the third element (what was first)
    
    This approach is simple and efficient for a fixed-size array of 3 elements.
    """
    # Create and return a new list with elements in rotated order
    # [second element, third element, first element]
    return [nums[1], nums[2], nums[0]]
    