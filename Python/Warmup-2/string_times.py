def string_times(str, n):
    """
    Creates a new string by repeating the input string n times.
    
    This function takes a string and multiplies it by a non-negative integer
    to create a concatenated result. Python's string multiplication operator (*)
    handles the repetition automatically.
    
    Parameters:
    -----------
    str : string
        The original string to be repeated. Can be any string including:
        - Empty string ('')
        - Single character ('a')
        - Multiple characters ('Hello')
        - Strings with spaces or special characters
    
    n : int
        The number of times to repeat the string. Must be non-negative.
        - If n = 0, returns empty string
        - If n = 1, returns the original string unchanged
        - If n > 1, returns the string concatenated n times
    
    Returns:
    --------
    string
        A new string containing n copies of the original string concatenated
        together with no separators between copies.
    
    Examples:
    ---------
    >>> string_times('Hi', 2)
    'HiHi'
    
    >>> string_times('Hi', 3)
    'HiHiHi'
    
    >>> string_times('Hi', 1)
    'Hi'
    
    >>> string_times('Hi', 0)
    ''
    
    >>> string_times('', 5)
    ''
    
    Notes:
    ------
    - Python's * operator for strings creates a new string object
    - The operation is O(n*m) where n is the repetition count and m is 
      the length of the original string
    - No validation is performed on inputs; assumes n is non-negative
    - If n is negative, Python will return an empty string
    """
    # Use Python's built-in string multiplication to repeat the string n times
    # This is more efficient and cleaner than manually looping and concatenating
    return str * n
