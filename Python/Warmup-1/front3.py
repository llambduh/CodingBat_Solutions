def front3(str):
    """
    Returns a new string consisting of 3 copies of the "front" of the input string.
    
    The "front" is defined as:
    - The first 3 characters if the string has 3 or more characters
    - The entire string if it has fewer than 3 characters
    
    Args:
        str: The input string to process
        
    Returns:
        A new string with the front repeated 3 times
        
    Examples:
        front3('Java') → 'JavJavJav'
        front3('Chocolate') → 'ChoChoCho'
        front3('abc') → 'abcabcabc'
        front3('ab') → 'ababab'
        front3('a') → 'aaa'
    """
    
    # Check if the string length is less than 3 characters
    # This handles edge cases where we don't have a full "front" of 3 chars
    if len(str) < 3:
        # If string is shorter than 3 chars (e.g., 'ab' or 'a'),
        # use the entire string as the "front" and repeat it 3 times
        # Example: 'ab' * 3 = 'ababab'
        return str * 3
    
    # For strings with 3 or more characters:
    # Extract the first 3 characters using slice notation str[0:3]
    # - str[0:3] means: start at index 0, go up to (but not including) index 3
    # - This gives us characters at indices 0, 1, and 2 (the first 3 chars)
    # Then multiply by 3 to create 3 consecutive copies
    # Example: 'Chocolate'[0:3] = 'Cho', then 'Cho' * 3 = 'ChoChoCho'
    return str[0:3] * 3
