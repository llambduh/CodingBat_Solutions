def no_teen_sum(a, b, c): 
  def fix_teen(n): 
    # Check if the number is within the teen range (13 to 19 inclusive)
    if n in range(13, 20): 
      # If it's a teen but not 15 or 16, treat it as 0
      if n not in [15, 16]: 
        return 0 
      # If it's 15 or 16, treat it as itself (not a teen)
      else: 
        return n 
    # If not a teen, return the number unchanged
    return n 
  # Apply the fix_teen function to each of the three inputs and return their sum
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
