def first_two(str):
    """
    Returns the first two characters of a given string.
    
    Purpose:
    --------
    This function extracts and returns the first two characters from the input string.
    It handles edge cases automatically, including strings shorter than 2 characters
    and empty strings.
    
    Parameters:
    -----------
    str : string
        The input string from which to extract the first two characters.
        Can be of any length, including 0 (empty string).
    
    Returns:
    --------
    string
        - If the string has 2 or more characters: returns the first two characters
        - If the string has exactly 1 character: returns that single character
        - If the string is empty: returns an empty string
    
    Examples:
    ---------
    first_two('Hello')   → 'He'     (string with 5 characters)
    first_two('abcdefg') → 'ab'     (string with 7 characters)
    first_two('ab')      → 'ab'     (string with exactly 2 characters)
    first_two('X')       → 'X'      (string with 1 character)
    first_two('')        → ''       (empty string)
    
    How it works:
    -------------
    The function uses Python's string slicing notation [start:end] where:
    - str[:2] means "slice from the beginning (index 0) up to but not including index 2"
    - This extracts characters at indices 0 and 1 (the first two characters)
    - Python's slicing is "safe" - it doesn't throw errors if the string is too short
    - If the string has fewer than 2 characters, slicing returns whatever is available
    
    Time Complexity:  O(1) - constant time, always extracts at most 2 characters
    Space Complexity: O(1) - creates a new string of at most 2 characters
    """
    
    # Use Python's slice notation to extract the first two characters
    # [:2] means "from the start up to (but not including) index 2"
    # This automatically handles all edge cases:
    #   - Strings >= 2 chars: returns first two characters
    #   - Strings with 1 char: returns that one character
    #   - Empty strings: returns empty stringd
    return str[:2]
    