def cigar_party(cigars, is_weekend):
    """
    Determines if a squirrel party is successful based on the number of cigars available.
    
    Parameters:
    -----------
    cigars : int
        The number of cigars available for the party
    is_weekend : bool
        True if the party is on a weekend, False if it's a weekday
    
    Returns:
    --------
    bool
        True if the party is successful, False otherwise
    
    Rules:
    ------
    - On weekdays: successful if cigars are between 40 and 60 (inclusive)
    - On weekends: successful if cigars are at least 40 (no upper limit)
    """
    
    # Check if it's the weekend
    if is_weekend:
        # Weekend parties are successful with 40 or more cigars (no upper bound)
        return cigars >= 40
    else:
        # Weekday parties are successful only if cigars are between 40 and 60 (inclusive)
        # Both conditions must be true: at least 40 AND at most 60
        return cigars >= 40 and cigars <= 60


# Example Test Cases:
# -------------------

# Case 1: cigar_party(30, False) → False
# - Weekday party with 30 cigars
# - 30 < 40, so doesn't meet minimum requirement
# - Returns False

# Case 2: cigar_party(50, False) → True
# - Weekday party with 50 cigars
# - 40 ≤ 50 ≤ 60, falls within the valid range
# - Returns True

# Case 3: cigar_party(70, True) → True
# - Weekend party with 70 cigars
# - 70 ≥ 40, meets minimum requirement (no maximum on weekends)
# - Returns True
