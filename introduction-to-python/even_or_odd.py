def is_even(number):
    """
    Check if a number is even or odd.
    
    Args:
        number (int): The number to check
        
    Returns:
        str: "even" if the number is even, "odd" if the number is odd
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
