def round_sum(a, b, c): 
  """
  Rounds three integers to the nearest multiple of 10 and returns their sum.
  - Numbers with rightmost digit 5 or higher are rounded up to the next multiple of 10.
  - Numbers with rightmost digit less than 5 are rounded down to the previous multiple of 10.
  
  Example:
  - 15 → 20 (rightmost digit is 5)
  - 12 → 10 (rightmost digit is 2 < 5)
  
  Uses a helper function `round10(num)` to handle the rounding logic for each number.
  """
  
  def round10(num): 
    """
    Rounds an integer to the nearest multiple of 10.
    
    Args:
        num (int): The number to round.
        
    Returns:
        int: The rounded value.
    """
    # Extract the rightmost digit
    rightmost_digit = num % 10
    
    # If rightmost digit is 5 or more, round up to the next multiple of 10
    if rightmost_digit >= 5: 
      return (num // 10 + 1) * 10
    
    # If rightmost digit is less than 5, round down to the previous multiple of 10
    else: 
      return num // 10 * 10
  
  # Apply the rounding function to each number and return their sum
  return round10(a) + round10(b) + round10(c)
