def front_back(str):
    """
    Exchange the first and last characters of a string.
    
    This function takes a string and returns a new string where the first
    and last characters have been swapped. For strings of length 1 or empty
    strings, the original string is returned unchanged since there's nothing
    to swap.
    
    Parameters:
    -----------
    str : string
        The input string whose first and last characters will be exchanged.
        Can be empty or any length.
    
    Returns:
    --------
    string
        A new string with the first and last characters swapped. If the string
        has length 0 or 1, returns the original string unchanged.
    
    Examples:
    ---------
    front_back('code') → 'eodc'   # 'c' and 'e' are swapped
    front_back('a') → 'a'         # single character, nothing to swap
    front_back('ab') → 'ba'       # two characters are swapped
    """
    
    # Check if string is too short to swap (length 0 or 1)
    # - Empty string: no characters to swap
    # - Single character: swapping would result in the same string
    if(len(str) <= 1):
        return str
    
    # For strings of length 2 or more, build the result by concatenating three parts:
    # 1. str[-1] - the LAST character (negative indexing: -1 is the last character)
    # 2. str[1:-1] - the MIDDLE section (everything except first and last character)
    # 3. str[0] - the FIRST character
    
    return str[-1] + str[1:-1] + str[0]
    
    # How it works for front_back('code'):
    # str[-1] returns 'e' (last character)
    # str[1:-1] returns 'od' (from index 1 up to but not including last index)
    # str[0] returns 'c' (first character)
    # 'e' + 'od' + 'c' = 'eodc'
    