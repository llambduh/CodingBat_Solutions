def monkey_trouble(a_smile, b_smile):
  """
  Determines if we are in trouble based on whether two monkeys are smiling.
  
  Problem: We are in trouble if BOTH monkeys are smiling OR if NEITHER is smiling.
           In other words, we're in trouble when both monkeys are in the SAME state.
  
  Parameters:
  -----------
  a_smile : bool
      True if monkey 'a' is smiling, False if monkey 'a' is not smiling
  b_smile : bool
      True if monkey 'b' is smiling, False if monkey 'b' is not smiling
  
  Returns:
  --------
  bool
      True if we are in trouble, False if we are safe
  
  Logic Breakdown:
  ----------------
  We are in trouble when:
  1. Both monkeys ARE smiling (a_smile = True AND b_smile = True)
  2. Both monkeys are NOT smiling (a_smile = False AND b_smile = False)
  
  Key Insight:
  ------------
  Notice that we're in trouble when BOTH monkeys have the SAME state!
  - If a_smile == b_smile, they're doing the same thing → TROUBLE
  - If a_smile != b_smile, they're doing different things → SAFE
  
  This means we can use a simple equality check instead of complex OR logic.
  
  Truth Table:
  ------------
  a_smile | b_smile | a_smile == b_smile | Are we in trouble?
  --------|---------|--------------------|-----------------
  True    | True    | True               | YES (both smiling)
  False   | False   | True               | YES (neither smiling)
  True    | False   | False              | NO (different states)
  False   | True    | False              | NO (different states)
  
  Examples:
  ---------
  monkey_trouble(True, True) → True    # Both smiling = trouble!
  monkey_trouble(False, False) → True  # Neither smiling = also trouble!
  monkey_trouble(True, False) → False  # Different states = we're safe
  monkey_trouble(False, True) → False  # Different states = we're safe
  """
  
  # Return True if both monkeys are in the same state (both smile or both don't)
  # This elegant solution uses equality to check if values match
  return (a_smile == b_smile)
  
  # Alternative (more verbose) way to write the same logic:
  # return (a_smile and b_smile) or (not a_smile and not b_smile)
  # But the equality check is much simpler and more readable!
  