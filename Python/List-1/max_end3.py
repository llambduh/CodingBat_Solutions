def max_end3(nums):
    """
    Sets all elements in a 3-element array to the maximum of the first or last element.
    
    This function compares the first and last elements of an array, determines
    which is larger, and then replaces ALL elements in the array with that
    larger value. The original array is modified in-place.
    
    Parameters:
    -----------
    nums : list
        An array/list of integers with exactly 3 elements.
        Example: [1, 2, 3]
    
    Returns:
    --------
    list
        The same list (modified in-place) with all elements set to the
        maximum of the original first or last element.
        Example: [3, 3, 3]
    
    Examples:
    ---------
    >>> max_end3([1, 2, 3])
    [3, 3, 3]
    # 3 (last) > 1 (first), so all elements become 3
    
    >>> max_end3([11, 5, 9])
    [11, 11, 11]
    # 11 (first) > 9 (last), so all elements become 11
    
    >>> max_end3([2, 11, 3])
    [3, 3, 3]
    # 3 (last) > 2 (first), so all elements become 3
    # Note: The middle element (11) is ignored in the comparison
    
    Implementation Details:
    ----------------------
    - Uses max() to compare first and last elements only
    - Middle elements are ignored in the comparison
    - Modifies the original list in-place using slice assignment
    
    Time Complexity: O(n) where n=3, so effectively O(1)
    Space Complexity: O(n) for creating the temporary list, so O(1) for fixed size
    """
    
    # Step 1: Determine which end value is larger
    # nums[0] = first element (index 0)
    # nums[-1] = last element (negative indexing: -1 means last position)
    # max() returns the larger of the two values
    bigger_num = max(nums[0], nums[-1])
    
    # Step 2: Replace ALL elements in the array with the larger value
    # nums[:] = slice notation that refers to the entire list
    #   - Using nums[:] modifies the ORIGINAL list in-place
    #   - This is different from nums = ... which would create a NEW list
    # [bigger_num] * len(nums) = creates a list with bigger_num repeated len(nums) times
    #   - Example: [3] * 3 = [3, 3, 3]
    #   - len(nums) ensures it works for any length (though spec says length 3)
    nums[:] = [bigger_num] * len(nums)
    
    # Step 3: Return the modified array
    # Note: The array was already modified in-place, so this returns
    # a reference to the same modified list object
    return nums
    