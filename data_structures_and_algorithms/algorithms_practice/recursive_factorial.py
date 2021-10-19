"""Recursive factorial module"""


class NegativeValueError(ValueError):
    """Negative value exception error"""


def factorial(number):
    """Returns factorial of number"""
    if not isinstance(number, int):
        raise TypeError('argument must be positive integer number')
    if number < 0:
        raise NegativeValueError('number argument must be non negative')

    if number > 0:
        return number * factorial(number - 1)

    return 1
