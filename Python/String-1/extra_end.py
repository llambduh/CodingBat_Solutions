def extra_end(str):
    """
    Create a new string consisting of 3 copies of the last 2 characters 
    of the original string.
    
    Parameters:
    -----------
    str : string
        The input string (guaranteed to have at least 2 characters)
    
    Returns:
    --------
    string
        A string containing the last 2 characters repeated 3 times
    
    Examples:
    ---------
    extra_end('Hello') → 'lololo'  # 'lo' repeated 3 times
    extra_end('ab') → 'ababab'      # 'ab' repeated 3 times
    extra_end('Hi') → 'HiHiHi'      # 'Hi' repeated 3 times
    """
    
    # str[-2:] - String slicing to get the last 2 characters
    #   - Negative indexing: -2 means "2nd position from the end"
    #   - The colon (:) creates a slice from index -2 to the end
    #   - If the string has exactly 2 chars, this returns the entire string
    #   - If the string has more than 2 chars, this returns only the last 2
    #
    # * 3 - String multiplication operator
    #   - Repeats the string 3 times
    #   - Example: 'ab' * 3 creates 'ababab'
    #
    # The entire operation is done in one line and returned immediately
    
    return str[-2:] * 3