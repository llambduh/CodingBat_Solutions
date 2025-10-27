def make_abba(a, b):
    """
    Creates a new string by concatenating two input strings in the pattern 'abba'.
    
    This function takes two strings and combines them by placing the first string,
    then the second string twice, and finally the first string again, forming
    the pattern: a + b + b + a
    
    Parameters:
    -----------
    a : str
        The first string to be used in positions 1 and 4 of the result
    b : str
        The second string to be used in positions 2 and 3 of the result
    
    Returns:
    --------
    str
        A concatenated string following the 'abba' pattern
    
    Examples:
    ---------
    >>> make_abba('Hi', 'Bye')
    'HiByeByeHi'
    
    >>> make_abba('Yo', 'Alice')
    'YoAliceAliceYo'
    
    >>> make_abba('What', 'Up')
    'WhatUpUpWhat'
    """
    
    # Concatenate strings in 'abba' order:
    # - Start with string 'a'
    # - Add string 'b' twice in the middle
    # - End with string 'a' again
    # The '+' operator is used for string concatenation in Python
    return a + b + b + a
