def love6(a, b):
  # First check if either of the two numbers is exactly 6.
  # The problem states that if either input value equals 6,
  # the function should immediately return True.
  if a == 6 or b == 6: 
    return True
  
  # Next check the sum and the difference of the numbers.
  #
  # Condition 1: If the sum of a and b equals 6, return True.
  # Example: a = 1, b = 5 → 1 + 5 = 6
  #
  # Condition 2: If the absolute difference between a and b equals 6,
  # return True. The abs() function is used so that the order
  # of subtraction does not matter.
  #
  # Example:
  # a = 10, b = 4 → abs(10 - 4) = 6
  # a = 4, b = 10 → abs(4 - 10) = 6
  if a + b == 6 or abs(a - b) == 6:
    return True
    
  # If none of the conditions above are true,
  # then the numbers are not related to 6 in any required way.
  # Therefore the function returns False.
  return False
  