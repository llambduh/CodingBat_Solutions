def array_count9(nums):
    """
    Count the number of times the value 9 appears in an array of integers.
    
    This function takes an array (list) of integers and returns how many times
    the number 9 occurs in that array.
    
    Parameters:
    -----------
    nums : list of int
        An array (list) of integers to search through. Can be empty or contain
        any number of elements.
    
    Returns:
    --------
    int
        The count of how many times the number 9 appears in the array.
        Returns 0 if the array is empty or contains no 9's.
    
    Examples:
    ---------
    >>> array_count9([1, 2, 9])
    1
    >>> array_count9([1, 9, 9])
    2
    >>> array_count9([1, 9, 9, 3, 9])
    3
    >>> array_count9([1, 2, 3])
    0
    >>> array_count9([])
    0
    
    Implementation Notes:
    --------------------
    Uses Python's built-in list.count() method, which efficiently iterates
    through the list and counts occurrences of the specified value (9).
    This is more concise and typically faster than manually looping through
    the array.
    
    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) - no additional space needed
    """
    # Use the built-in count() method to count occurrences of 9 in the list
    return nums.count(9)
