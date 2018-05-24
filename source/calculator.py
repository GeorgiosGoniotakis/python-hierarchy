"""
This is an example Calculator app which performs addition,
subtraction, multiplication and division. It will help me
demonstrate how to appropriately structure a Python project.
The coding style of the project is PEP8.
"""

__author__ = 'Georgios Goniotakis'
__email__ = 'georgios.goniotakis@outlook.com'
__license__ = 'MIT'
__date__ = 'Thursday, May 24, 2018'
__version__ = '1.0'

import requests

from source.utils.calculation import Calculation


def main(event, context):
    """
    Runs an HTTP request and four arithmetic operations. Receives
    two arguments which are used only if you want to run your script
    using AWS Lambda. Feel free to remove them if you do not use this
    service.
    :param event: AWS event parameter
    :param context: AWS context parameter
    """

    # Perform an HTTP request for absolutely no reason
    http = requests.get(url="https://www.google.com")

    # Perform a set of arithmetic operations and output their
    # result.
    print("Result of addition: {}".format(Calculation.addition(1, 2, 3, 4)))
    print("Result of subtraction: {}".format(Calculation.subtraction(2, 1)))
    print("Result of multiplication: {}".format(Calculation.multiplication(2, 3)))
    print("Result of division: {}".format(Calculation.division(4, 2)))
