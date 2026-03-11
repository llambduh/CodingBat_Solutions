def caught_speeding(speed, is_birthday):
    # Determine the extra speed allowance if it is the driver's birthday.
    # The problem states that on your birthday you can drive 5 mph faster
    # before receiving the same penalty.
    # If is_birthday is True, birthday_bonus = 5
    # If is_birthday is False, birthday_bonus = 0
    birthday_bonus = 5 if is_birthday else 0

    # Check if the driver's speed is within the "no ticket" range.
    # Normally this is 60 mph or less.
    # On a birthday the limit increases by 5 mph (65 mph or less).
    # If the speed is within this adjusted limit, return 0 (no ticket).
    if speed <= 60 + birthday_bonus:
        return 0

    # Check if the driver's speed falls within the "small ticket" range.
    # Normally this is between 61 and 80 mph inclusive.
    # On a birthday this range shifts up by 5 mph (66–85 mph).
    # If the speed is within this adjusted range, return 1 (small ticket).
    if speed <= 80 + birthday_bonus:
        return 1

    # If the speed is greater than the upper limit of the small ticket range,
    # the driver receives a big ticket.
    # Normally this is 81 mph or more, or 86 mph or more on a birthday.
    return 2
    