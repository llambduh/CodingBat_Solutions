def combo_string(a, b):
  """
  Creates a combo string in the format: short + long + short.
  
  This function takes two strings of different lengths and combines them by
  placing the shorter string at the beginning and end, with the longer string
  in the middle (sandwich pattern).
  
  Parameters:
  -----------
  a : string
      The first input string. Can be empty (length 0).
  b : string
      The second input string. Can be empty (length 0).
      Note: The problem guarantees a and b will not be the same length.
  
  Returns:
  --------
  string
      A concatenated string in the format: shorter + longer + shorter
  
  Examples:
  ---------
  combo_string('Hello', 'hi') → 'hiHellohi'  # 'hi' is shorter (length 2)
  combo_string('hi', 'Hello') → 'hiHellohi'  # Order doesn't matter
  combo_string('aaa', 'b') → 'baaab'         # Single char as wrapper
  combo_string('', 'Hello') → 'Hello'        # Empty string as wrapper
  combo_string('abc', '') → 'abc'            # Empty string as wrapper
  
  Algorithm:
  ----------
  1. Compare the lengths of both strings
  2. Identify which string is longer and which is shorter
  3. Concatenate in the pattern: short + long + short
  
  Time Complexity: O(n + m) where n and m are the lengths of the strings
  Space Complexity: O(n + m) for the resulting concatenated string
  """
  
  # Determine which string is longer and which is shorter
  # Compare the lengths of both input strings
  if len(a) > len(b):
    # String 'a' is longer, so 'a' goes in the middle
    long = a
    short = b
  else:
    # String 'b' is longer OR they are equal (though problem says they won't be equal)
    # In this case, 'a' is shorter or equal, so 'a' goes on the outside
    short = a
    long = b
  
  # Concatenate strings in the sandwich pattern: short + long + short
  # The shorter string wraps around the longer string
  # Example: short='hi', long='Hello' → 'hi' + 'Hello' + 'hi' = 'hiHellohi'
  return short + long + short
  