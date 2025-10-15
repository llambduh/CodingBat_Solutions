def missing_char(str, n):
    """
    Remove a character at a specified index from a string.
    
    This function takes a non-empty string and an integer index, then returns
    a new string with the character at that index removed. The function uses
    string slicing to construct the result without modifying the original string.
    
    Parameters:
    -----------
    str : string
        A non-empty string from which a character will be removed.
        
    n : int
        The index of the character to remove. This will always be a valid index
        (0 <= n < len(str)), so no error checking is needed.
    
    Returns:
    --------
    string
        A new string identical to the input string except with the character
        at index n removed. The length of the returned string will be 
        len(str) - 1.
    
    Examples:
    ---------
    missing_char('kitten', 1) → 'ktten'   # removes 'i' at index 1
    missing_char('kitten', 0) → 'itten'   # removes 'k' at index 0
    missing_char('kitten', 4) → 'kittn'   # removes 'e' at index 4
    """
    
    # Solution uses string slicing to concatenate two parts:
    # 1. str[:n] - gets all characters from the beginning up to (but not including) index n
    # 2. str[n+1:] - gets all characters from index n+1 to the end
    # By concatenating these two slices, we effectively "skip" the character at index n
    
    return str[:n] + str[n+1:]
    
    # How it works for missing_char('kitten', 1):
    # str[:1] returns 'k' (characters from index 0 up to but not including index 1)
    # str[2:] returns 'tten' (characters from index 2 to the end)
    # 'k' + 'tten' = 'ktten'
    