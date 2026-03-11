def caught_speeding(speed, is_birthday):
  birthday_bonus = 5 if is_birthday else 0
  if speed <= 60 + birthday_bonus:
      return 0
  if speed <= 80 + birthday_bonus:
      return 1
  return 2