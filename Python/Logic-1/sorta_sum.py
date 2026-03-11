def sorta_sum(a, b):
  # Calculate the sum of the two input integers a and b.
  # This represents the normal result before applying the special rule.
  sum = a + b

  # Check if the calculated sum falls within the forbidden range.
  # The problem states that sums between 10 and 19 inclusive
  # (meaning 10, 11, 12, ..., 19) are not allowed.
  #
  # If the sum is within this range, the function must return 20 instead
  # of the actual sum.
  #
  # The ternary conditional expression works as follows:
  # - If (sum >= 10 and sum <= 19) is True → return 20
  # - Otherwise → return the original sum
  return 20 if sum >= 10 and sum <= 19 else sum