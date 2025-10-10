def sleep_in(weekday, vacation):
  """
  Determines whether we can sleep in based on weekday and vacation status.
  
  Problem: We sleep in if it is NOT a weekday OR if we are on vacation.
  
  Parameters:
  -----------
  weekday : bool
      True if it is a weekday (Monday-Friday), False if it's a weekend
  vacation : bool
      True if we are on vacation, False if we are not on vacation
  
  Returns:
  --------
  bool
      True if we can sleep in, False otherwise
  
  Logic Breakdown:
  ----------------
  We can sleep in when EITHER condition is true:
  1. It's NOT a weekday (i.e., it's the weekend)
  2. We ARE on vacation (regardless of what day it is)
  
  This is a classic OR operation with one negation:
  - "not weekday" means it's the weekend
  - "vacation" means we're on vacation
  - The OR (|) operator returns True if at least one condition is True
  
  Truth Table:
  ------------
  weekday | vacation | not weekday | not weekday OR vacation | Result
  --------|----------|-------------|------------------------|--------
  False   | False    | True        | True                   | Sleep in (weekend, no vacation)
  True    | False    | False       | False                  | No sleep in (weekday, no vacation)
  False   | True     | True        | True                   | Sleep in (weekend, on vacation)
  True    | True     | False       | True                   | Sleep in (weekday, but on vacation)
  
  Examples:
  ---------
  sleep_in(False, False) → True   # Weekend, no vacation = sleep in!
  sleep_in(True, False) → False   # Weekday, no vacation = wake up early
  sleep_in(False, True) → True    # Weekend, on vacation = definitely sleep in!
  sleep_in(True, True) → True     # Weekday, but on vacation = sleep in!
  """
  
  # Return True if it's NOT a weekday (weekend) OR if we're on vacation
  # The parentheses are optional here but included for clarity
  return (not weekday or vacation)
  
  # Alternative way to think about it:
  # We DON'T sleep in only when: it's a weekday AND we're not on vacation
  # So we COULD also write: return not (weekday and not vacation)
  # Both approaches are correct, but the original is more intuitive