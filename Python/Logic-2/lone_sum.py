def lone_sum(a, b, c):
    """
    Calculates the sum of three integers, excluding any values that appear
    more than once among the three inputs.

    A value is considered "lone" if it is unique — meaning it does not match
    either of the other two values. If a value appears 2 or 3 times, it is
    excluded entirely from the sum (all occurrences are ignored).

    Args:
        a (int): The first integer value.
        b (int): The second integer value.
        c (int): The third integer value.

    Returns:
        int: The sum of only the unique (non-duplicate) values.

    Examples:
        lone_sum(1, 2, 3) → 6   # All three values are unique, so 1 + 2 + 3 = 6
        lone_sum(3, 2, 3) → 2   # 3 appears twice, so it's excluded; only 2 counts
        lone_sum(3, 3, 3) → 0   # 3 appears three times, all excluded; sum is 0
    """

    # Store the three input values in a list for easy iteration and counting
    nums = [a, b, c]

    # Use a generator expression inside sum() to:
    #   - Iterate over each number 'n' in the list
    #   - Use nums.count(n) to check how many times 'n' appears in the list
    #   - Only include 'n' in the sum if it appears exactly once (i.e., it's "lone")
    #   - If count > 1, the value is a duplicate and is excluded from the sum
    return sum(n for n in nums if nums.count(n) == 1)
    