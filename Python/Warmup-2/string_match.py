def string_match(a, b):
    """
    Count the number of positions where two strings contain the same length-2 substring.
    
    Args:
        a (str): The first string to compare
        b (str): The second string to compare
    
    Returns:
        int: The count of matching 2-character substrings at the same positions
    
    Examples:
        string_match('xxcaazz', 'xxbaaz') → 3  # 'xx', 'aa', 'az' match
        string_match('abc', 'abc') → 2          # 'ab', 'bc' match
        string_match('abc', 'axc') → 0          # no matches
    """
    
    # Find the length of the shorter string to avoid index out of bounds errors
    # We can only compare substrings up to the length of the shorter string
    # Example: if a='xxcaazz' (len=7) and b='xxbaaz' (len=6), shorter=6
    shorter = min(len(a), len(b))
    
    # Use a generator expression with sum() to count matches efficiently
    # - range(shorter - 1): iterate from 0 to shorter-2
    #   We use (shorter - 1) because we're extracting 2-char substrings
    #   If shorter=6, we can check positions 0,1,2,3,4 (5 positions total)
    #   Position 5 would need characters at index 5 and 6, but index 6 doesn't exist
    # 
    # - a[i:i+2]: extracts a 2-character substring from string a starting at index i
    #   Example: if a='xxcaazz' and i=0, a[0:2] gives 'xx'
    #            if i=1, a[1:3] gives 'xc'
    #
    # - b[i:i+2]: extracts the corresponding 2-character substring from string b
    #
    # - a[i:i+2] == b[i:i+2]: compares if the substrings at position i are identical
    #   Returns True (counts as 1) if they match, False (counts as 0) if they don't
    #
    # - sum(...): adds up all the True values (which equal 1) to get the total count
    return sum(a[i:i+2] == b[i:i+2] for i in range(shorter - 1))
