def in1to10(n, outside_mode):
  # First check if the function is operating in "outside mode".
  # When outside_mode is True, the rule changes from checking
  # inside the range to checking outside the range.
  if outside_mode:

    # In outside mode, return True if the number is
    # less than or equal to 1 OR greater than or equal to 10.
    #
    # This means values at the edges or beyond the range count as True.
    #
    # Examples:
    # n = 1  → True
    # n = 0  → True
    # n = 10 → True
    # n = 11 → True
    return n <= 1 or n >= 10
  
  # If outside_mode is False, use the normal rule.
  # Return True only if the number is within the range 1 to 10 inclusive.
  #
  # "Inclusive" means the endpoints (1 and 10) are included.
  #
  # Examples:
  # n = 1  → True
  # n = 5  → True
  # n = 10 → True
  # n = 11 → False
  return n >= 1 and n <= 10