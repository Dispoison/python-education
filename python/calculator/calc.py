"""This module contains a class with basic mathematical operations"""


class Calc:
    """
    A class with basic mathematical operations.

    ...

    Methods
    -------
    add(first_number, second_number):
        Returns the sum of two numbers.
    sub(first_number, second_number):
        Returns the difference of two numbers.
    mul(first_number, second_number):
        Returns the product of two numbers.
    div(first_number, second_number):
        Returns the quotient of two numbers.
    """

    @staticmethod
    def add(first_number, second_number):
        """Returns the sum of two numbers"""
        return first_number + second_number

    @staticmethod
    def sub(first_number, second_number):
        """Returns the difference of two numbers"""
        return first_number - second_number

    @staticmethod
    def mul(first_number, second_number):
        """Returns product of two values"""
        return first_number * second_number

    @staticmethod
    def div(first_number, second_number):
        """Returns the quotient of two numbers"""
        if second_number == 0:
            print('Division by zero')
            return None
        return first_number / second_number


print(Calc.add(5, 3))
print(Calc.sub(4, 1))
print(Calc.mul(6, 8))
print(Calc.div(18, 3))
