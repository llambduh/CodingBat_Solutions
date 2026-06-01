def close_far(a, b, c): 
  # Check if one of b or c is close (difference from a <= 1) and the other is far (difference from both a and the other value >= 2)
  if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2: 
    return True 
  elif abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2: 
    return True 
  else: 
    return False
