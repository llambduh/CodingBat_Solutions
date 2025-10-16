def front_times(str, n):
    """
    Returns n copies of the 'front' portion of a string.
    
    The 'front' is defined as the first 3 characters of the string,
    or the entire string if it has fewer than 3 characters.
    
    Parameters:
    -----------
    str : string
        The input string from which to extract the front portion
    n : int
        A non-negative integer specifying how many times to repeat the front
    
    Returns:
    --------
    string
        A string containing n repetitions of the front portion
    
    Examples:
    ---------
    front_times('Chocolate', 2) → 'ChoCho'
    front_times('Chocolate', 3) → 'ChoChoCho'
    front_times('Abc', 3) → 'AbcAbcAbc'
    front_times('Ab', 3) → 'AbAbAb'
    front_times('', 3) → ''
    """
    
    # Check if the string has 3 or fewer characters
    if len(str) <= 3:
        # If string is short enough, use the entire string as the 'front'
        # The * operator repeats the string n times
        # Example: 'Ab' * 3 = 'AbAbAb'
        return str * n
    
    # If the string has more than 3 characters
    # Extract only the first 3 characters using slicing [0:3]
    # Then repeat those 3 characters n times
    # Example: 'Chocolate'[0:3] = 'Cho', then 'Cho' * 2 = 'ChoCho'
    return str[0:3] * n
