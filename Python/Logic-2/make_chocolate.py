def make_chocolate(small, big, goal):
    """
    Calculate the number of small bars needed to reach the desired weight (goal)
    given a limited supply of small and big chocolate bars.

    Parameters:
    small (int): Number of 1-kilo small chocolate bars available.
    big (int): Number of 5-kilo big chocolate bars available.
    goal (int): Desired total weight in kilos of chocolate to be made.

    Returns:
    int: The number of small bars needed if it's possible to make the desired weight,
         otherwise returns -1 indicating it's not feasible.

    Examples:
    make_chocolate(4, 1, 9) → 4
    make_chocolate(4, 1, 10) → -1
    make_chocolate(4, 1, 7) → 2
    """

    # Calculate the maximum number of big bars that can be used without exceeding the goal
    big = min(big, goal // 5)

    # Calculate the remaining weight needed after using the maximum number of big bars
    remainder = goal - (big * 5)

    # Check if the remaining weight can be made up exactly using small bars
    if remainder <= small:
        return remainder
    else:
        # If the remainder cannot be met with available small bars, return -1.
        return -1
    