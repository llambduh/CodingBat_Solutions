def combo_string(a, b):
  if len(a) > len(b):
    long = a
    short = b
  else:
    short = a
    long = b
    
  return short + long + short