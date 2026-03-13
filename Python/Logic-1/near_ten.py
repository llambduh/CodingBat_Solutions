def near_ten(num):
    # The goal is to determine whether the given number is
    # within 2 of a multiple of 10.
    #
    # Examples of multiples of 10:
    # 0, 10, 20, 30, 40, ...
    #
    # Numbers that are within 2 of these would be:
    # 8, 9, 10, 11, 12  (near 10)
    # 18, 19, 20, 21, 22 (near 20)

    # The modulo operator (%) returns the remainder after division.
    # num % 10 gives the distance from the previous multiple of 10.
    #
    # Examples:
    # 12 % 10 = 2   → 2 away from 10
    # 17 % 10 = 7   → 7 away from 10
    # 19 % 10 = 9   → 1 away from 20 (since 20 - 19 = 1)

    # If the remainder is 0, 1, or 2, the number is within
    # 2 ABOVE a multiple of 10 (e.g., 10, 11, 12).
    #
    # If the remainder is 8 or 9, the number is within
    # 2 BELOW the NEXT multiple of 10 (e.g., 18, 19).
    #
    # Therefore:
    # remainder <= 2  → close to the lower multiple
    # remainder >= 8  → close to the next multiple

    return num % 10 <= 2 or num % 10 >= 8
    