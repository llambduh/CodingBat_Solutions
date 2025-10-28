def make_out_word(out, word):
    """
    Inserts a word into the middle of a 4-character 'out' string.
    
    This function takes a 4-character string that typically represents
    opening and closing delimiters (like '<<>>' or '[[]]'), splits it
    in half, and inserts the given word between the two halves.
    
    Parameters:
    -----------
    out : str
        A string of exactly 4 characters representing the outer wrapper.
        The first 2 characters form the "opening" delimiter.
        The last 2 characters form the "closing" delimiter.
        Examples: '<<>>', '[[]]', '(())', '{{}}', '::::', '----'
    
    word : str
        The word or text to be inserted in the middle of the 'out' string.
        Can be any length (single word or multiple words).
    
    Returns:
    --------
    str
        A new string with the word sandwiched between the first half
        and second half of the 'out' string.
        Format: out[0:2] + word + out[2:4]
    
    Examples:
    ---------
    >>> make_out_word('<<>>', 'Yay')
    '<<Yay>>'
    
    >>> make_out_word('<<>>', 'WooHoo')
    '<<WooHoo>>'
    
    >>> make_out_word('[[]]', 'word')
    '[[word]]'
    
    >>> make_out_word('(())', 'text')
    '((text))'
    """
    
    # String slicing breakdown:
    # ------------------------
    # out[0:2] - Extracts characters at indices 0 and 1 (first 2 chars)
    #            For '<<>>': out[0:2] returns '<<'
    #            For '[[]]': out[0:2] returns '[['
    #
    # word     - The middle content to insert
    #            Example: 'Yay', 'WooHoo', 'word'
    #
    # out[2:4] - Extracts characters at indices 2 and 3 (last 2 chars)
    #            For '<<>>': out[2:4] returns '>>'
    #            For '[[]]': out[2:4] returns ']]'
    #
    # Concatenation process for make_out_word('<<>>', 'Yay'):
    #   out[0:2]  →  '<<'
    #   word      →  'Yay'
    #   out[2:4]  →  '>>'
    #   Result    →  '<<' + 'Yay' + '>>' = '<<Yay>>'
    
    return out[0:2] + word + out[2:4]
