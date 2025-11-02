def first_half(str):
    """
    Returns the first half of a string of even length.
    
    This function takes a string with an even number of characters and returns
    the first half by dividing the string at its midpoint.
    
    Args:
        str (string): An input string of even length
        
    Returns:
        string: The first half of the input string
        
    Examples:
        first_half('WooHoo') → 'Woo'
        first_half('HelloThere') → 'Hello'
        first_half('abcdef') → 'abc'
    """
    
    # Calculate the midpoint of the string using integer division
    # len(str) gets the total length of the string
    # // is the floor division operator, which divides and rounds down to nearest integer
    # For example: if len(str) = 6, then 6 // 2 = 3
    
    # Use string slicing to extract the first half
    # str[:n] returns characters from index 0 up to (but not including) index n
    # Since we're using len(str)//2 as the endpoint, we get exactly half the string
    return str[:len(str)//2]
    