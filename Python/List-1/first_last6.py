def first_last6(nums):
    """
    Determines if the number 6 appears as the first or last element in an array.
    
    Parameters:
    -----------
    nums : list of int
        An array/list of integers with length >= 1
    
    Returns:
    --------
    bool
        True if 6 is the first element OR the last element
        False otherwise
    
    Examples:
    ---------
    first_last6([1, 2, 6]) → True  (6 is the last element)
    first_last6([6, 1, 2, 3]) → True  (6 is the first element)
    first_last6([13, 6, 1, 2, 3]) → False  (6 is in the middle, not first or last)
    """
    
    # Check if the first element equals 6 OR if the last element equals 6
    # nums[0] accesses the first element (index 0)
    # nums[-1] accesses the last element (negative indexing in Python)
    # The 'or' operator returns True if either condition is True
    # This boolean expression is directly returned
    return nums[0] == 6 or nums[-1] == 6


# EXPLANATION OF KEY CONCEPTS:
# 
# 1. Array Indexing:
#    - nums[0]: First element (positive indexing starts at 0)
#    - nums[-1]: Last element (negative indexing counts from the end)
#
# 2. Boolean Logic:
#    - The expression evaluates to True if EITHER condition is met
#    - We don't need both positions to be 6, just one of them
#    - Short-circuit evaluation: if nums[0] == 6 is True, 
#      Python won't even check nums[-1]
#
# 3. Edge Cases Handled:
#    - Single element array: [6] → nums[0] and nums[-1] refer to the 
#      same element, so it correctly returns True
#    - Array with 6 in both positions: [6, 2, 6] → Returns True 
#      (only needs one condition to be met)
#
# 4. Why This Solution is Elegant:
#    - O(1) time complexity (constant time access)
#    - No loops needed
#    - Concise and readable
#    - Leverages Python's negative indexing feature
