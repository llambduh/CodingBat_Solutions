def close_far(a, b, c): 
  """
  Returns True if exactly one of b or c is "close" to a (difference <= 1), 
  and the other is "far" from both a and the close value (difference >= 2).
  
  Rules:
  - "Close" means the absolute difference from 'a' is at most 1.
  - "Far" means the absolute difference from 'a' is at least 2, 
    and also the absolute difference from the other value is at least 2.
  
  Example:
  - close_far(1, 2, 10): 2 is close to 1 (diff = 1), 10 is far from 1 (diff = 9) and from 2 (diff = 8) → True
  - close_far(1, 2, 3): Both 2 and 3 are close to 1 → False
  
  Uses absolute difference (abs) to compute distances.
  """
  # Check if b is close to a and c is far from both a and b
  if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2: 
    return True 
  # Check if c is close to a and b is far from both a and c
  elif abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2: 
    return True 
  # If neither condition is met, return False
  else: 
    return False
