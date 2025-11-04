def without_end(str):
  """
  Returns a new string with the first and last characters removed.
  
  This function takes a string of at least length 2 and returns a substring
  that excludes the first character (index 0) and the last character (index -1).
  
  Parameters:
  -----------
  str : string
      The input string to process. Must have a length of at least 2.
  
  Returns:
  --------
  string
      A new string containing all characters except the first and last.
      If the input string has length 2, returns an empty string.
      If the input string has length 3+, returns the middle character(s).
  
  Examples:
  ---------
  without_end('Hello') → 'ell'    # Returns characters at indices 1,2,3
  without_end('java') → 'av'      # Returns characters at indices 1,2
  without_end('coding') → 'odin'  # Returns characters at indices 1,2,3,4
  without_end('Hi') → ''          # Returns empty string (no middle chars)
  
  How it works:
  -------------
  The slicing notation str[1:-1] works as follows:
  - str[1:...] starts at index 1 (second character), skipping index 0
  - str[...:-1] ends at index -1 (one position before the last character)
  - Combined: str[1:-1] extracts everything between (but not including) 
    the first and last positions
  
  Time Complexity: O(n) where n is the length of the string
  Space Complexity: O(n) for the new string created
  """
  
  # Use Python slice notation to extract substring from index 1 to second-to-last
  # [1:-1] means: start at position 1, end before position -1 (last character)
  return str[1:-1]
  