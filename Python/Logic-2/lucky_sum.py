def lucky_sum(a, b, c):
    """
    Returns the sum of a, b, c — except if a value equals 13,
    that value AND everything to its right is excluded from the sum.

    Examples:
        lucky_sum(1, 2, 3)  → 6  (no 13, full sum)
        lucky_sum(1, 2, 13) → 3  (13 at index 2, only a+b count)
        lucky_sum(1, 13, 3) → 1  (13 at index 1, only a counts)
    """

    # Store the three values in order so we can slice and sum them easily.
    # Order matters here — we need to preserve left-to-right position.
    values = [a, b, c]

    # Find the "cut point" — the index where 13 first appears.
    # If 13 is found, everything from that index onwards is ignored.
    # If 13 is not found, we keep the full list (cut = 3).
    #
    # Example: [1, 13, 3] → cut = 1
    # Example: [1,  2, 3] → cut = 3
    cut = values.index(13) if 13 in values else len(values)

    # Slice the list up to (but not including) the cut point,
    # then sum the remaining values..
    #
    # Example: values[:1] → [1]       → sum = 1
    # Example: values[:3] → [1, 2, 3] → sum = 6
    return sum(values[:cut])
