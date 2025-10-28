def make_tags(tag, word):
    """
    Creates an HTML string with opening and closing tags surrounding a word.
    
    This function takes a tag name and a word, then constructs a properly
    formatted HTML string where the word is wrapped in the specified tags.
    
    Parameters:
    -----------
    tag : str
        The HTML tag name (without angle brackets) to wrap around the word.
        Examples: 'i', 'b', 'cite', 'strong', 'em', etc.
    
    word : str
        The text content to be enclosed within the HTML tags.
        Can be a single word or multiple words/phrases.
    
    Returns:
    --------
    str
        A complete HTML string with opening tag, content, and closing tag.
        Format: '<tag>word</tag>'
    
    Examples:
    ---------
    >>> make_tags('i', 'Yay')
    '<i>Yay</i>'
    
    >>> make_tags('i', 'Hello')
    '<i>Hello</i>'
    
    >>> make_tags('cite', 'Yay')
    '<cite>Yay</cite>'
    
    >>> make_tags('strong', 'Important')
    '<strong>Important</strong>'
    """
    
    # Construct the complete HTML string by concatenating:
    # 1. '<' + tag + '>'  - Creates the opening tag (e.g., '<i>')
    # 2. word             - Adds the content between tags (e.g., 'Yay')
    # 3. '</' + tag + '>' - Creates the closing tag (e.g., '</i>')
    # 
    # String concatenation order:
    #   '<'  +  'i'  +  '>'  +  'Yay'  +  '</'  +  'i'  +  '>'
    #   Results in: '<i>Yay</i>'
    
    return '<' + tag + '>' + word + "</" + tag + '>'
