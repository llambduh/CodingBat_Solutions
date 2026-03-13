def make_bricks(small, big, goal):
    """
    Determine whether it's possible to build a row of bricks that is
    exactly 'goal' inches long, using any combination of:
        - Small bricks : 1 inch each
        - Big bricks   : 5 inches each

    Approach (No Loops Required):
    ------------------------------
    Rather than trying every combination, we use simple math:
        1. Greedily use as many big bricks as possible (without overshooting).
        2. Check whether the remaining gap can be filled with small bricks.

    Parameters:
    -----------
    small (int) : Number of available small bricks (1 inch each)
    big   (int) : Number of available big bricks   (5 inches each)
    goal  (int) : The exact target row length in inches

    Returns:
    --------
    bool : True  → It IS     possible to reach exactly 'goal' inches
           False → It IS NOT possible to reach exactly 'goal' inches

    Examples:
    ---------
    make_bricks(3, 1, 8)  → True
        1 big brick (5") + 3 small bricks (3") = 8" ✅

    make_bricks(3, 1, 9)  → False
        1 big brick (5") + 4 small bricks needed, but only 3 available ❌

    make_bricks(3, 2, 10) → True
        2 big bricks (10") + 0 small bricks = 10" ✅
    """

    # -------------------------------------------------------------------------
    # STEP 1: Determine the ideal number of big bricks to use.
    #
    # We use min() to enforce TWO hard constraints simultaneously:
    #
    # Constraint A → min(..., big)
    #   We cannot use more big bricks than we actually HAVE.
    #   e.g. If big=1, we can use at most 1 big brick regardless of the goal.
    #
    # Constraint B → min(goal // 5, ...)
    #   We cannot use more big bricks than physically FIT within the goal.
    #   Floor division (//) gives the maximum whole big bricks that fit.
    #
    #   e.g. goal=8  → 8  // 5 = 1  → at most 1 big brick fits (5"), not 2 (10")
    #   e.g. goal=10 → 10 // 5 = 2  → exactly 2 big bricks fit (10")
    #   e.g. goal=9  → 9  // 5 = 1  → at most 1 big brick fits (5"), remainder=4
    #
    # Why not just always use all available big bricks?
    #   → Using too many big bricks could OVERSHOOT the goal.
    #   → e.g. goal=8, big=2 → using both = 10" which already exceeds 8" ❌
    #      So we cap at goal//5 = 1 big brick instead.
    #
    # Result: big_needed holds the largest safe number of big bricks to use.
    # -------------------------------------------------------------------------
    big_needed = min(big, goal // 5)

    # -------------------------------------------------------------------------
    # STEP 2: Check if small bricks can cover the remaining distance.
    #
    # After placing 'big_needed' big bricks:
    #
    #   Total inches covered by big bricks = big_needed * 5
    #   Remaining gap to fill              = goal - (big_needed * 5)
    #
    # Since small bricks are each 1 inch, we need exactly (goal - big_needed*5)
    # small bricks to fill the remaining gap.
    #
    # The check "<= small" asks:
    #   "Do we have ENOUGH small bricks to cover the remainder?"
    #
    # Why "<=" instead of "=="?
    #   → We don't need to use ALL small bricks, just enough.
    #   → If remainder = 2 and small = 5, we can simply use 2 of the 5 → ✅
    #   → If remainder = 0, no small bricks needed at all             → ✅
    #   → If remainder = 4 but small = 3, we're 1 short               → ❌
    #
    # Visual Breakdown per Example:
    # ┌────────────────────────┬───────────┬───────────┬───────────┬────────┐
    # │ Call                   │ big_needed│ Coverage  │ Remainder │ Result │
    # ├────────────────────────┼───────────┼───────────┼───────────┼────────┤
    # │ make_bricks(3, 1, 8)   │     1     │  1×5 = 5" │ 8-5  = 3" │  True  │
    # │ make_bricks(3, 1, 9)   │     1     │  1×5 = 5" │ 9-5  = 4" │  False │
    # │ make_bricks(3, 2, 10)  │     2     │  2×5 =10" │ 10-10= 0" │  True  │
    # └────────────────────────┴───────────┴───────────┴───────────┴────────┘
    #
    # This single expression replaces what would otherwise need a loop. ✅
    # -------------------------------------------------------------------------
    return (goal - big_needed * 5) <= small
    