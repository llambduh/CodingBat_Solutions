def diff21(n):
  """
  Returns the absolute difference between n and 21, with special doubling rule.
  
  Problem: Calculate how far n is from 21, but if n is OVER 21,
           double that difference.
  
  Parameters:
  -----------
  n : int
      Any integer value (can be positive, negative, or zero)
  
  Returns:
  --------
  int
      If n > 21: returns abs(n - 21) * 2 (double the absolute difference)
      If n <= 21: returns abs(n - 21) (regular absolute difference)
  
  What is Absolute Difference?
  ----------------------------
  Absolute difference means the distance between two numbers, always positive.
  - abs(19 - 21) = abs(-2) = 2
  - abs(25 - 21) = abs(4) = 4
  - abs(21 - 21) = abs(0) = 0
  
  The abs() function removes the negative sign if present.
  
  Logic Breakdown:
  ----------------
  1. Check if n is greater than 21
  2. If YES (n > 21):
     - Calculate: n - 21 (this will be positive since n > 21)
     - Take absolute value: abs(n - 21) (technically redundant here)
     - Double it: abs(n - 21) * 2
  3. If NO (n <= 21):
     - Calculate: n - 21 (this will be negative or zero)
     - Take absolute value: abs(n - 21) (makes it positive)
     - Return it as is
  
  Examples with Detailed Calculations:
  ------------------------------------
  Example 1: diff21(19) → 2
    - Is 19 > 21? NO
    - Calculate: abs(19 - 21) = abs(-2) = 2
    - Return: 2
  
  Example 2: diff21(10) → 11
    - Is 10 > 21? NO
    - Calculate: abs(10 - 21) = abs(-11) = 11
    - Return: 11
  
  Example 3: diff21(21) → 0
    - Is 21 > 21? NO
    - Calculate: abs(21 - 21) = abs(0) = 0
    - Return: 0
  
  Example 4: diff21(25) → 8
    - Is 25 > 21? YES
    - Calculate: abs(25 - 21) = abs(4) = 4
    - Double it: 4 * 2 = 8
    - Return: 8
  
  Example 5: diff21(30) → 18
    - Is 30 > 21? YES
    - Calculate: abs(30 - 21) = abs(9) = 9
    - Double it: 9 * 2 = 18
    - Return: 18
  
  Example 6: diff21(0) → 21
    - Is 0 > 21? NO
    - Calculate: abs(0 - 21) = abs(-21) = 21
    - Return: 21
  
  Example 7: diff21(-5) → 26
    - Is -5 > 21? NO
    - Calculate: abs(-5 - 21) = abs(-26) = 26
    - Return: 26
  
  Visual Number Line:
  -------------------
  ... -5 ← [26 away] → 0 ← [21 away] → 10 ← [11 away] → 19 ← [2] → 21 ← [8 doubled from 4] → 25 ...
                                                                      ↑
                                                                 Target: 21
  
  Why abs() is Used:
  ------------------
  - When n < 21: (n - 21) gives a NEGATIVE number, abs() makes it positive
  - When n = 21: (n - 21) = 0, abs() keeps it at 0
  - When n > 21: (n - 21) gives a POSITIVE number, abs() doesn't change it
                 (abs() is technically not needed in this case, but included for consistency)
  """
  
  # Check if n is greater than 21 (special doubling rule applies)
  if n > 21:
    # n is over 21, so return DOUBLE the absolute difference
    # Since n > 21, (n - 21) is already positive, but abs() ensures it
    return abs(n - 21) * 2
  else:
    # n is 21 or less, so return the regular absolute difference
    # abs() is crucial here because (n - 21) will be negative when n < 21
    return abs(n - 21)
