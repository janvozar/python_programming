import doctest

def multiply_numbers(numbers):
    """
    >>> multiply_numbers([2, 4, 6, 8])
    384
    """
    result = 0
    for number in numbers:
        result = result * number
    return result

doctest.testmod()