def makes10(a, b):
  """
  Determines if either number is 10 or if the two numbers sum to 10.
  
  Problem: Return True if ANY of the following conditions is met:
           1. The first number (a) equals 10
           2. The second number (b) equals 10
           3. The sum of both numbers (a + b) equals 10
  
  Parameters:
  -----------
  a : int
      The first integer value
  b : int
      The second integer value
  
  Returns:
  --------
  bool
      True if one of them is 10 OR their sum is 10
      False if none of the conditions are met
  
  Logic Breakdown:
  ----------------
  We return True if ANY of these three conditions is True:
  - Condition 1: a == 10 (first number is 10)
  - Condition 2: b == 10 (second number is 10)
  - Condition 3: a + b == 10 (numbers add up to 10)
  
  Using OR operator:
  - If ANY condition is True, the entire expression is True
  - ALL conditions must be False for the result to be False
  - This is a "one or more" check (at least one condition satisfied)
  
  Structure: (a == 10 or b == 10) or (a + b == 10)
  - First part: (a == 10 or b == 10) checks if either number IS 10
  - Second part: (a + b == 10) checks if they ADD UP to 10
  - Outer or: Combines both checks
  
  Truth Table for OR:
  -------------------
  Condition A | Condition B | A or B
  ------------|-------------|-------
  False       | False       | False
  False       | True        | True
  True        | False       | True
  True        | True        | True
  
  Examples with Detailed Analysis:
  ---------------------------------
  Example 1: makes10(9, 10) → True
    - Is a == 10? Is 9 == 10? No (False)
    - Is b == 10? Is 10 == 10? Yes (True) ✓
    - (a == 10 or b == 10) = (False or True) = True
    - Since we already have True, we don't need to check sum
    - Result: True (because b is 10)
  
  Example 2: makes10(9, 9) → False
    - Is a == 10? Is 9 == 10? No (False)
    - Is b == 10? Is 9 == 10? No (False)
    - (a == 10 or b == 10) = (False or False) = False
    - Is a + b == 10? Is 9 + 9 == 10? Is 18 == 10? No (False)
    - Final: False or False = False
    - Result: False (neither is 10, and sum is not 10)
  
  Example 3: makes10(1, 9) → True
    - Is a == 10? Is 1 == 10? No (False)
    - Is b == 10? Is 9 == 10? No (False)
    - (a == 10 or b == 10) = (False or False) = False
    - Is a + b == 10? Is 1 + 9 == 10? Is 10 == 10? Yes (True) ✓
    - Final: False or True = True
    - Result: True (sum equals 10)
  
  Example 4: makes10(10, 0) → True
    - Is a == 10? Yes ✓
    - (a == 10 or b == 10) = (True or False) = True
    - Result: True (a is 10)
  
  Example 5: makes10(10, 10) → True
    - Is a == 10? Yes ✓
    - Is b == 10? Yes ✓
    - (a == 10 or b == 10) = (True or True) = True
    - Note: Their sum is 20, but we don't need to check it
    - Result: True (both are 10)
  
  Example 6: makes10(5, 5) → True
    - Is a == 10? No (False)
    - Is b == 10? No (False)
    - (a == 10 or b == 10) = False
    - Is a + b == 10? Is 5 + 5 == 10? Yes ✓
    - Final: False or True = True
    - Result: True (sum equals 10)
  
  Example 7: makes10(3, 4) → False
    - Is a == 10? No (False)
    - Is b == 10? No (False)
    - (a == 10 or b == 10) = False
    - Is a + b == 10? Is 3 + 4 == 10? Is 7 == 10? No (False)
    - Final: False or False = False
    - Result: False (no condition met)
  
  Example 8: makes10(10, 5) → True
    - Is a == 10? Yes ✓
    - Result: True (a is 10, don't need to check further)
    - Note: Sum is 15, but it doesn't matter
  
  Example 9: makes10(-1, 11) → True
    - Is a == 10? No (False)
    - Is b == 10? No (False)
    - (a == 10 or b == 10) = False
    - Is a + b == 10? Is -1 + 11 == 10? Is 10 == 10? Yes ✓
    - Result: True (sum equals 10)
  
  Example 10: makes10(0, 10) → True
    - Is a == 10? No (False)
    - Is b == 10? Yes ✓
    - Result: True (b is 10)
  
  Why Group with Parentheses?
  ----------------------------
  The outer parentheses around (a == 10 or b == 10) are technically optional
  because comparison operators (==) have higher precedence than logical operators (or).
  
  Without parentheses:
  return a == 10 or b == 10 or a + b == 10
  
  This works the same way! But the original grouping makes it clearer that we're
  checking two separate things:
  1. Is either number 10? (a == 10 or b == 10)
  2. Does the sum equal 10? (a + b == 10)
  
  Short-Circuit Evaluation:
  --------------------------
  Python evaluates OR expressions from left to right and stops as soon as
  it finds a True value (this is called "short-circuit evaluation").
  
  If a == 10 is True, Python returns True immediately without checking b or the sum.
  If a == 10 is False but b == 10 is True, Python returns True without checking the sum.
  Only if both a and b are not 10 does Python need to check if a + b == 10.
  """
  
  # Return True if either number is 10 OR if their sum is 10
  # The expression uses OR logic to check multiple conditions
  return (a == 10 or b == 10) or (a + b == 10)
  
  # Breaking it down:
  # Part 1: (a == 10 or b == 10) - checks if either individual number is 10
  # Part 2: (a + b == 10) - checks if the sum equals 10
  # Combined with OR: returns True if ANY condition is met
