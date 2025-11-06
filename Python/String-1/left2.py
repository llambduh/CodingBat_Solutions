def left2(str):
    """
    Rotates a string left by 2 positions by moving the first 2 characters to the end.
    
    Args:
        str (string): The input string to be rotated. Must have at least 2 characters.
    
    Returns:
        string: A new string with the first 2 characters moved to the end.
    
    Examples:
        left2('Hello') → 'lloHe'
        left2('java') → 'vaja'
        left2('Hi') → 'Hi'
    """
    
    # String slicing approach to rotate left by 2 positions:
    # 
    # str[2:] - Extracts all characters from index 2 to the end of the string
    #           This gives us everything EXCEPT the first 2 characters
    #           Example: 'Hello'[2:] → 'llo'
    #
    # str[:2] - Extracts the first 2 characters (from start up to, but not including, index 2)
    #           This gives us just the first 2 characters
    #           Example: 'Hello'[:2] → 'He'
    #
    # By concatenating str[2:] + str[:2], we effectively move the first 2 chars to the end
    # Example: 'llo' + 'He' → 'lloHe'
    
    return str[2:] + str[:2]


# Alternative implementation with intermediate variables for clarity:
def left2_verbose(str):
    """Same functionality as left2, but with explicit intermediate variables."""
    
    # Extract everything after the first 2 characters
    remaining_chars = str[2:]  # Characters from index 2 onwards
    
    # Extract the first 2 characters
    first_two_chars = str[:2]  # Characters at indices 0 and 1
    
    # Concatenate: remaining characters + first two characters
    rotated_string = remaining_chars + first_two_chars
    
    return rotated_string


# Key Concepts:
# 1. String Slicing: str[start:end] extracts a substring
#    - str[2:] means "from index 2 to the end"
#    - str[:2] means "from the beginning up to (but not including) index 2"
#
# 2. String Immutability: This creates a NEW string; the original is unchanged
#
# 3. Time Complexity: O(n) where n is the length of the string
#    - Both slicing operations scan through the string once
#
# 4. Space Complexity: O(n) for the new string created
