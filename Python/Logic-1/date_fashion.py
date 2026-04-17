def date_fashion(you, date):
    """
    Determines if you and your date can get a table at a restaurant
    based on the stylishness of your clothes.
    
    Parameters:
    -----------
    you : int
        The stylishness of your clothes, in the range 0..10
    date : int
        The stylishness of your date's clothes, in the range 0..10
    
    Returns:
    --------
    int
        0 = no (cannot get a table)
        1 = maybe (might get a table)
        2 = yes (will get a table)
    """
    
    # IMPORTANT: This condition must be checked FIRST
    # If either person is very unstylish (2 or less), the result is always "no"
    # This takes priority over being stylish, so we check it before the stylish condition
    if you <= 2 or date <= 2:
        return 0  # No table - someone is too unstylish
    
    # If we reach here, neither person is unstylish (both are > 2)
    # Now check if either person is very stylish (8 or more)
    # If so, the result is "yes" - stylishness gets you a table
    elif you >= 8 or date >= 8:
        return 2  # Yes - at least one person is very stylish
    
    # If we reach here:
    # - Neither person is unstylish (both > 2)
    # - Neither person is very stylish (both < 8)
    # So both stylishness values are in the range 3-7 (inclusive)
    # The result is "maybe"
    return 1  # Maybe - average stylishness for both
    