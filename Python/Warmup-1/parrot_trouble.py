def parrot_trouble(talking, hour):
  """
  Determines if we are in trouble based on a parrot talking at certain hours.
  
  Problem: We are in trouble if the parrot is talking AND it's either
           too early (before 7 AM) OR too late (after 8 PM).
           We're NOT in trouble if the parrot is quiet, regardless of time.
  
  Parameters:
  -----------
  talking : bool
      True if the parrot is currently talking, False if the parrot is quiet
  hour : int
      Current hour in 24-hour format (0-23)
      - 0 = midnight, 6 = 6 AM, 12 = noon, 20 = 8 PM, 23 = 11 PM
  
  Returns:
  --------
  bool
      True if we are in trouble (parrot talking during quiet hours)
      False if we are safe (parrot quiet OR acceptable time)
  
  Time Ranges Explained:
  ----------------------
  Acceptable hours (not in trouble): 7 AM to 8 PM (hours 7-20 inclusive)
  Problem hours (we're in trouble):
    - Before 7 AM: hours 0, 1, 2, 3, 4, 5, 6 (hour < 7)
    - After 8 PM: hours 21, 22, 23 (hour > 20)
  
  Visual Timeline (24-hour format):
  ---------------------------------
  Hour:  0  1  2  3  4  5  6 | 7  8  9 10 11 12 13 14 15 16 17 18 19 20 | 21 22 23
  Time:  12 1  2  3  4  5  6 | 7  8  9 10 11 12  1  2  3  4  5  6  7  8 |  9 10 11
         AM AM AM AM AM AM AM | AM AM AM AM AM PM PM PM PM PM PM PM PM | PM PM PM
         ←── TOO EARLY ──────→ ←────── ACCEPTABLE HOURS ──────────────→ ←─ TOO LATE ─→
         (hour < 7)             (hour >= 7 AND hour <= 20)              (hour > 20)
  
  Logic Breakdown:
  ----------------
  We need BOTH conditions to be True for trouble:
  
  Condition 1: talking == True
    - The parrot must be talking
    - If the parrot is quiet (False), we're never in trouble
  
  Condition 2: (hour < 7 or hour > 20)
    - The hour must be in the "quiet hours" range
    - hour < 7: Before 7 AM (early morning)
    - hour > 20: After 8 PM (late evening)
    - The OR means either condition makes it a bad time
  
  Combined with AND:
    - talking AND (bad_time)
    - Both must be True for us to be in trouble
  
  Truth Table:
  ------------
  talking | hour < 7 | hour > 20 | (hour < 7 or hour > 20) | Result (in trouble?)
  --------|----------|-----------|-------------------------|--------------------
  False   | True     | False     | True                    | False (quiet parrot)
  False   | False    | False     | False                   | False (quiet parrot)
  False   | False    | True      | True                    | False (quiet parrot)
  True    | False    | False     | False                   | False (acceptable time)
  True    | True     | False     | True                    | True (talking + too early)
  True    | False    | True      | True                    | True (talking + too late)
  
  Examples with Detailed Analysis:
  ---------------------------------
  Example 1: parrot_trouble(True, 6) → True
    - Parrot is talking: True ✓
    - Hour is 6 (6 AM)
    - Is 6 < 7? Yes ✓ (too early!)
    - Is 6 > 20? No
    - (6 < 7 or 6 > 20) = (True or False) = True
    - True AND True = True → WE'RE IN TROUBLE!
  
  Example 2: parrot_trouble(True, 7) → False
    - Parrot is talking: True ✓
    - Hour is 7 (7 AM)
    - Is 7 < 7? No (7 is not less than 7)
    - Is 7 > 20? No
    - (7 < 7 or 7 > 20) = (False or False) = False
    - True AND False = False → We're safe (acceptable time)
  
  Example 3: parrot_trouble(False, 6) → False
    - Parrot is talking: False (parrot is quiet)
    - Hour is 6 (6 AM)
    - Is 6 < 7? Yes ✓
    - Is 6 > 20? No
    - (6 < 7 or 6 > 20) = (True or False) = True
    - False AND True = False → We're safe (quiet parrot)
  
  Example 4: parrot_trouble(True, 21) → True
    - Parrot is talking: True ✓
    - Hour is 21 (9 PM)
    - Is 21 < 7? No
    - Is 21 > 20? Yes ✓ (too late!)
    - (21 < 7 or 21 > 20) = (False or True) = True
    - True AND True = True → WE'RE IN TROUBLE!
  
  Example 5: parrot_trouble(True, 20) → False
    - Parrot is talking: True ✓
    - Hour is 20 (8 PM)
    - Is 20 < 7? No
    - Is 20 > 20? No (20 is not greater than 20)
    - (20 < 7 or 20 > 20) = (False or False) = False
    - True AND False = False → We're safe (8 PM is still OK)
  
  Example 6: parrot_trouble(False, 15) → False
    - Parrot is talking: False (quiet)
    - Hour is 15 (3 PM)
    - Since parrot is quiet, we're safe regardless of time
    - False AND (anything) = False → We're safe
  
  Operator Precedence:
  --------------------
  In Python: comparison operators (< >) are evaluated before logical operators (and, or)
  So: talking and (hour < 7 or hour > 20)
  Is evaluated as: talking and ((hour < 7) or (hour > 20))
  
  The parentheses around (hour < 7 or hour > 20) are technically optional
  but included for clarity.
  """
  
  # Return True only if BOTH conditions are met:
  # 1. The parrot is talking (talking == True)
  # 2. AND the time is outside acceptable hours (hour < 7 OR hour > 20)
  return talking and (hour < 7 or hour > 20)
  
  # This is equivalent to:
  # return (talking == True) and ((hour < 7) or (hour > 20))
  # But in Python, we can use boolean variables directly in conditions
