def sum_double(a, b):
  """
  Returns the sum of two integers, with a special rule for matching values.
  
  Problem: Add two numbers together, but if they are the same value,
           return DOUBLE their sum instead of the regular sum.
  
  Parameters:
  -----------
  a : int
      The first integer value
  b : int
      The second integer value
  
  Returns:
  --------
  int
      If a == b: returns (a + b) * 2 (double the sum)
      If a != b: returns a + b (regular sum)
  
  Logic Breakdown:
  ----------------
  1. Check if the two values are equal (a == b)
  2. If YES (they match):
     - Calculate their sum: a + b
     - Double that sum: (a + b) * 2
     - Example: sum_double(2, 2) → (2 + 2) * 2 → 4 * 2 → 8
  3. If NO (they don't match):
     - Just return their regular sum: a + b
     - Example: sum_double(1, 2) → 1 + 2 → 3
  
  Examples Table:
  ---------------
  a  | b  | a == b? | Calculation      | Result
  ---|----|---------|--------------------|-------
  1  | 2  | No      | 1 + 2              | 3
  3  | 2  | No      | 3 + 2              | 5
  2  | 2  | Yes     | (2 + 2) * 2 = 4*2  | 8
  5  | 5  | Yes     | (5 + 5) * 2 = 10*2 | 20
  -1 | -1 | Yes     | (-1+-1) * 2 = -2*2 | -4
  
  Why (a + b) * 2 for doubles?
  -----------------------------
  When numbers match, we want "double their sum":
  - If a = 2 and b = 2
  - Regular sum = 2 + 2 = 4
  - Double the sum = 4 * 2 = 8
  - Formula: (a + b) * 2
  
  Note: (a + b) * 2 is the same as 2 * (a + b)
        When a == b, this also equals 4 * a or 4 * b
        Example: (2 + 2) * 2 = 4 * 2 = 8
  """
  
  # Check if both values are the same
  if a == b:
    # Special case: values match, so return double their sum
    # (a + b) gives us the sum, then we multiply by 2 to double it
    return (a + b) * 2
  
  # Default case: values are different, return regular sum
  # No 'else' needed because if the condition above is True,
  # the function already returned and this line won't execute
  return a + b
