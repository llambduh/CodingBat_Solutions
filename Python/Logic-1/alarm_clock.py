def alarm_clock(day, vacation):
  # Determine whether the given day is a weekend.
  # According to the problem:
  # 0 = Sunday and 6 = Saturday
  # These two days are considered weekends.
  # If the day matches either of these values, is_weekend will be True.
  # Otherwise, it will be False (meaning it is a weekday).
  is_weekend = day == 0 or day == 6

  # First check if the person is on vacation.
  # Vacation changes the normal alarm schedule.
  if vacation:

      # If we are on vacation AND it is the weekend,
      # the alarm clock should be turned off completely.
      # So the function returns the string "off".
      if is_weekend:
          return "off"

      # If we are on vacation but it is a weekday,
      # the alarm should ring later than usual at 10:00.
      else:
          return "10:00"
  
  # If we are NOT on vacation, follow the normal schedule.

  # If it is the weekend (Saturday or Sunday),
  # the alarm should ring later at 10:00.
  if is_weekend:
      return "10:00"

  # Otherwise it must be a weekday (Monday–Friday),
  # and the alarm should ring at the normal time of 7:00.
  return "7:00"