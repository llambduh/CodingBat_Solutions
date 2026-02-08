def squirrel_play(temp, is_summer):
    """
    Determines whether squirrels in Palo Alto will play based on temperature.
    
    Squirrels play when the temperature falls within an acceptable range:
    - Standard range: 60 to 90 degrees (inclusive)
    - Summer range: 60 to 100 degrees (inclusive) - squirrels tolerate more heat
    
    Parameters:
    -----------
    temp : int
        The current temperature in degrees (assumed Fahrenheit)
    is_summer : bool
        True if it's currently summer, False otherwise
        
    Returns:
    --------
    bool
        True if squirrels will play, False if they won't
        
    Examples:
    ---------
    >>> squirrel_play(70, False)  # 70°F in non-summer: within 60-90 range
    True
    >>> squirrel_play(95, False)  # 95°F in non-summer: exceeds 90 upper limit
    False
    >>> squirrel_play(95, True)   # 95°F in summer: within expanded 60-100 range
    True
    """
    
    # Check if it's summer - this affects the upper temperature limit
    if is_summer:
        # SUMMER: Squirrels play between 60 and 100 degrees (inclusive)
        # The upper limit is raised to 100 because squirrels are more
        # heat-tolerant during summer months
        return temp >= 60 and temp <= 100
    else:
        # NON-SUMMER (Spring, Fall, Winter): Squirrels play between 60 and 90
        # degrees (inclusive). The lower upper limit reflects that squirrels
        # prefer cooler temperatures outside of summers
        return temp >= 60 and temp <= 90
        