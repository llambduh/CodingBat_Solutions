def not_string(s):
    """
    Add 'not ' to the front of a string if it doesn't already start with 'not'.
    
    This function takes a string and prepends "not " to it. However, if the 
    string already begins with "not", it returns the original string unchanged
    to avoid redundancy (e.g., "not not candy").
    
    Args:
        s (str): The input string to be processed
    
    Returns:
        str: Either the original string (if it starts with "not") or 
             a new string with "not " prepended to the front
    
    Examples:
        not_string('candy') → 'not candy'
        not_string('x') → 'not x'
        not_string('not bad') → 'not bad'
    """
    
    # Check if the string starts with the word "not"
    # The startswith() method returns True if the string begins with "not"
    # and False otherwise. This is case-sensitive, so "Not" would return False.
    if s.startswith("not"):
        # If the string already starts with "not", return it as-is
        # without any modifications to avoid duplication like "not not bad"
        return s
    
    # If the string does NOT start with "not", prepend "not " to the front
    # Note: We add "not " (with a space) to ensure proper word separation
    # between "not" and the original string content
    return "not " + s
