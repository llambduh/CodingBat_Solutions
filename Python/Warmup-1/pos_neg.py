def pos_neg(a, b, negative):
    """
    Determines if two integers have specific sign relationships.
    
    Parameters:
    -----------
    a : int
        The first integer value to check
    b : int
        The second integer value to check
    negative : bool
        A flag that changes the function's behavior:
        - If True: checks if BOTH numbers are negative
        - If False: checks if numbers have OPPOSITE signs (one positive, one negative)
    
    Returns:
    --------
    bool
        True if the sign condition is met, False otherwise
    
    Examples:
    ---------
    pos_neg(1, -1, False) → True   # One positive, one negative
    pos_neg(-1, 1, False) → True   # One negative, one positive
    pos_neg(-4, -5, True) → True   # Both negative when negative=True
    """
    
    # Check if the 'negative' parameter is True
    if(negative):
        # When negative=True, we want BOTH numbers to be negative
        # Returns True only when a < 0 AND b < 0
        return (a < 0 and b < 0)
    else:
        # When negative=False, we want numbers with OPPOSITE signs
        # This means: (a is negative AND b is positive) OR (a is positive AND b is negative)
        # 
        # Breaking down the condition:
        # - (a < 0 and b > 0): a is negative, b is positive
        # - (a > 0 and b < 0): a is positive, b is negative
        # - The 'or' combines these two cases
        return (a < 0 and b > 0) or (a > 0 and b < 0)
    