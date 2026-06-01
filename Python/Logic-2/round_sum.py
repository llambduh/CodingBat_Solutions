def round_sum(a, b, c): 
  def round10(num): 
    # Get the rightmost digit
    rightmost_digit = num % 10
    # If rightmost digit is 5 or more, round up to the next multiple of 10
    if rightmost_digit >= 5: 
      return (num // 10 + 1) * 10 
    # Otherwise, round down to the previous multiple of 10
    else: 
      return num // 10 * 10 
  return round10(a) + round10(b) + round10(c)
