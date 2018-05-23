"""
This file includes the implementation of the Calculation class.
"""


class Calculation:
    """
    Implements the most basic arithmetic operations.
    """

    @staticmethod
    def addition(*args):
        """
        Adds multiple numbers
        :param args: List of numbers
        :return: The sum of the arguments
        """
        return sum(args)

    @staticmethod
    def subtraction(x1, x2):
        """
        Subtracts two numbers
        :param x1: First number
        :param x2: Second number
        :return: Result of subtraction
        """
        return x1 - x2

    @staticmethod
    def multiplication(x1, x2):
        """
        Multiplies two numbers
        :param x1: First number
        :param x2: Second number
        :return: Result of multiplication
        """
        return x1 * x2

    @staticmethod
    def division(x1, x2):
        """
        Divides two numbers
        :param x1: First number
        :param x2: Second number
        :return: Result of division
        """
        return x1 / x2
