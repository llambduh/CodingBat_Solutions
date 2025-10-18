def string_splosion(str):
  """
  Creates a "string explosion" by progressively building substrings.
  
  Given a string, this function returns a new string that contains all 
  progressively longer prefixes of the input string concatenated together.
  
  Args:
    str: A non-empty string to explode
    
  Returns:
    A string containing all prefixes from length 1 to len(str) concatenated
    
  Examples:
    string_splosion('Code') → 'CCoCodCode'
      - Iteration 0: result = '' + 'C' = 'C'
      - Iteration 1: result = 'C' + 'Co' = 'CCo'
      - Iteration 2: result = 'CCo' + 'Cod' = 'CCoCod'
      - Iteration 3: result = 'CCoCod' + 'Code' = 'CCoCodCode'
    
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
  """
  
  # Initialize an empty string to accumulate all the progressive substrings
  result = ""
  
  # Loop through each index position in the input string
  # range(len(str)) generates indices from 0 to len(str)-1
  for i in range(len(str)):
    # str[:i+1] creates a slice from the beginning up to and including index i
    # This extracts progressively longer prefixes:
    #   - When i=0: str[:1] gives the first character
    #   - When i=1: str[:2] gives the first two characters
    #   - When i=2: str[:3] gives the first three characters, etc.
    # Concatenate this prefix to the result string
    result = result + str[:i+1]
  
  # Return the final concatenated string containing all prefixes
  return result
