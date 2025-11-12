def sum3(nums):
    """
    Calculate the sum of all elements in an array of exactly 3 integers.
    
    This function takes an array containing exactly 3 integer values and
    returns their total sum using Python's built-in sum() function.
    
    Parameters:
    -----------
    nums : list of int
        An array/list containing exactly 3 integer elements to be summed.
        Expected format: [int, int, int]
    
    Returns:
    --------
    int
        The sum of all three elements in the input array.
        Calculated as: nums[0] + nums[1] + nums[2]
    
    Examples:
    ---------
    >>> sum3([1, 2, 3])
    6
    
    >>> sum3([5, 11, 2])
    18
    
    >>> sum3([7, 0, 0])
    7
    
    Notes:
    ------
    - The function assumes the input array always contains exactly 3 elements
    - No validation is performed on the array length
    - The sum() function iterates through all elements and adds them together
    - Works with negative numbers as well: sum3([-1, 2, 3]) → 4
    """
    # Use Python's built-in sum() function to add all elements in the nums array
    # sum() iterates through the iterable and returns the total of all items
    return sum(nums)
    