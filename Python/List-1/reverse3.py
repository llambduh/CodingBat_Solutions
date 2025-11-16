def reverse3(nums):
    """
    Reverses an array of exactly 3 integers.
    
    This function takes an array containing 3 integer elements and returns
    a new array with the elements in reverse order. The original array
    remains unchanged.
    
    Parameters:
    -----------
    nums : list
        An array/list of integers with exactly 3 elements.
        Example: [1, 2, 3]
    
    Returns:
    --------
    list
        A new list containing the same elements in reverse order.
        Example: [3, 2, 1]
    
    Examples:
    ---------
    >>> reverse3([1, 2, 3])
    [3, 2, 1]
    
    >>> reverse3([5, 11, 9])
    [9, 11, 5]
    
    >>> reverse3([7, 0, 0])
    [0, 0, 7]
    
    Implementation Details:
    ----------------------
    Uses Python's slice notation with a step of -1 (nums[::-1]).
    - The first colon indicates "from the beginning"
    - The second colon indicates "to the end"
    - The -1 indicates "step backwards by 1"
    
    This creates a new list by traversing the original list from end to start.
    
    Time Complexity: O(n) where n=3, so effectively O(1)
    Space Complexity: O(n) for the new reversed list, so O(1) for fixed size
    """
    # Use slice notation to create a reversed copy of the array
    # [::-1] means: start from end, go to beginning, step by -1
    return nums[::-1]
    