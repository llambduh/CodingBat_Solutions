def string_bits(str):
  """
  Returns a new string containing every other character from the input string,
  starting with the first character (index 0).
  
  Args:
      str: The input string to process
      
  Returns:
      A new string made up of characters at even indices (0, 2, 4, etc.)
      
  Examples:
      string_bits('Hello') → 'Hlo' (takes H at index 0, l at index 2, o at index 4)
      string_bits('Hi') → 'H' (takes only H at index 0)
      string_bits('Heeololeo') → 'Hello' (takes characters at even positions)
  """
  
  # Initialize an empty string to accumulate the result
  # This will store every other character as we iterate through the input
  result = ""
  
  # Loop through all indices of the input string
  # range(len(str)) generates numbers from 0 to length-1
  # For example, if str = "Hello", range(5) gives us 0, 1, 2, 3, 4
  for i in range(len(str)):
    
    # Check if the current index is even (divisible by 2)
    # The modulo operator % gives the remainder of division
    # Even indices (0, 2, 4, 6...) will have remainder 0 when divided by 2
    if i % 2 == 0:
      
      # Add the character at the current even index to our result string
      # This builds our output one character at a time
      result += str[i]
  
  # Return the final string containing only the characters at even positions
  return result
