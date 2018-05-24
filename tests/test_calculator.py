"""
This file includes all the Unit Tests of the project.
"""

from unittest import TestCase

from source.utils.calculation import Calculation


class TestScript(TestCase):
    """
    Checks the functionality of the Calculator utility.
    """

    def test_addition(self):
        """
        Checks the functionality of the addition.
        """
        assert Calculation.addition(1, 1) == 2

    def test_subtraction(self):
        """
        Checks the functionality of the subtraction.
        """
        assert Calculation.subtraction(2, 1) == 1

    def test_multiplication(self):
        """
        Checks the functionality of the multiplication.
        """
        assert Calculation.multiplication(2, 3) == 6

    def test_division(self):
        """
        Checks the functionality of the division.
        """
        assert Calculation.division(6, 3) == 2
