def hello_name(name):
    """
    Generate a greeting string in the format "Hello [name]!"
    
    This function takes a name as input and returns a formatted greeting
    by concatenating the word "Hello", the provided name, and an exclamation mark.
    
    Parameters:
    -----------
    name : str
        The name to be included in the greeting message.
        Can be any string value (e.g., "Bob", "Alice", "X")
    
    Returns:
    --------
    str
        A greeting string in the format "Hello [name]!"
        
    Examples:
    ---------
    >>> hello_name('Bob')
    'Hello Bob!'
    >>> hello_name('Alice')
    'Hello Alice!'
    >>> hello_name('X')
    'Hello X!'
    """
    # Concatenate "Hello ", the name parameter, and "!" using the + operator
    # This creates a new string by joining three string components together
    return "Hello " + name + "!"


# ============================================================================
# PYTHON 3.6+ VERSION (Using f-strings)
# ============================================================================

def hello_name(name):
    """
    Generate a greeting string using f-string formatting (Python 3.6+)
    
    This version uses f-strings (formatted string literals), which provide
    a more modern and readable way to embed expressions inside string literals.
    F-strings are prefixed with 'f' and use curly braces {} to embed variables.
    
    Parameters:
    -----------
    name : str
        The name to be included in the greeting message
    
    Returns:
    --------
    str
        A greeting string in the format "Hello [name]!"
        
    Advantages of f-strings:
    ------------------------
    - More readable and concise syntax
    - Faster execution than traditional concatenation
    - Easier to maintain and debug
    - Can embed complex expressions within the braces
        
    Examples:
    ---------
    >>> hello_name('Bob')
    'Hello Bob!'
    >>> hello_name('Alice')
    'Hello Alice!'
    >>> hello_name('X')
    'Hello X!'
    """
    # Use an f-string to embed the name variable directly into the string
    # The 'f' prefix indicates this is a formatted string literal
    # {name} gets replaced with the actual value of the name parameter
    return f"Hello {name}!"
