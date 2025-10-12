def near_hundred(n):
    """
    Determines if a given number is within 10 of either 100 or 200.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if n is within 10 of 100 or 200, False otherwise
    """
    
    # Check if n is within 10 of 100 OR within 10 of 200
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    
    # BREAKDOWN OF THE LOGIC:
    
    # Part 1: abs(100 - n) <= 10
    # - This calculates the absolute distance between 100 and n
    # - abs() ensures we get a positive distance regardless of whether n is
    #   greater than or less than 100
    # - This condition is True when n is in the range [90, 110]
    # - Examples:
    #   * n = 93: abs(100 - 93) = abs(7) = 7 <= 10 ✓ True
    #   * n = 110: abs(100 - 110) = abs(-10) = 10 <= 10 ✓ True
    #   * n = 89: abs(100 - 89) = abs(11) = 11 <= 10 ✗ False
    
    # Part 2: abs(200 - n) <= 10
    # - This calculates the absolute distance between 200 and n
    # - This condition is True when n is in the range [190, 210]
    # - Examples:
    #   * n = 195: abs(200 - 195) = abs(5) = 5 <= 10 ✓ True
    #   * n = 210: abs(200 - 210) = abs(-10) = 10 <= 10 ✓ True
    #   * n = 180: abs(200 - 180) = abs(20) = 20 <= 10 ✗ False
    
    # The 'or' operator:
    # - Returns True if EITHER condition is True
    # - Returns False only if BOTH conditions are False
    # - This means n only needs to be near ONE of the target numbers (100 or 200)
    
    # EXAMPLE WALKTHROUGH:
    # near_hundred(93):
    #   abs(100 - 93) = 7 <= 10 → True
    #   abs(200 - 93) = 107 <= 10 → False
    #   True or False → True ✓
    
    # near_hundred(90):
    #   abs(100 - 90) = 10 <= 10 → True
    #   abs(200 - 90) = 110 <= 10 → False
    #   True or False → True ✓
    
    # near_hundred(89):
    #   abs(100 - 89) = 11 <= 10 → False
    #   abs(200 - 89) = 111 <= 10 → False
    #   False or False → False ✓
    
    # WHY USE abs()?
    # - Without abs(), we'd need to check both directions:
    #   (100 - n <= 10 AND n - 100 <= 10)
    # - abs() simplifies this by making the distance always positive
    # - It handles both cases: when n < 100 and when n > 100
    