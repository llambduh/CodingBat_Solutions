def non_start(a, b):
    """
    Concatenates two strings after removing the first character from each.
    
    This function takes two strings as input and returns a new string that
    consists of both input strings concatenated together, but with the first
    character of each string omitted.
    
    Parameters:
    -----------
    a : str
        The first string (must be at least length 1)
    b : str
        The second string (must be at least length 1)
    
    Returns:
    --------
    str
        A concatenated string containing all characters from 'a' except the 
        first character, followed by all characters from 'b' except the first
        character.
    
    Examples:
    ---------
    >>> non_start('Hello', 'There')
    'ellohere'
    
    >>> non_start('java', 'code')
    'avaode'
    
    >>> non_start('shotl', 'java')
    'hotlava'
    
    How it works:
    -------------
    - a[1:] creates a slice of string 'a' starting from index 1 to the end,
      effectively removing the character at index 0 (the first character)
    - b[1:] does the same for string 'b'
    - The + operator concatenates these two sliced strings
    - The result is returned as a single string
    
    Note:
    -----
    - String slicing in Python uses zero-based indexing
    - a[1:] is safe even for single-character strings (returns empty string)
    - No explicit error handling needed as problem guarantees length >= 1
    """
    # Slice both strings from index 1 onwards to exclude first character
    # Then concatenate them using the + operator
    return a[1:] + b[1:]
    