"""
Created by Neel Gokhale at 2020-07-19
File functions.py from project Project_Calculator
Built using PyCharm

"""


def add(num1: float, num2: float) -> float:
    """
    Adds 2 numbers and returns the add

    :param num1: first number
    :param num2: second number
    :return: addition of numbers
    """
    return num1 + num2


def subtract(num1: float, num2: float, in_order: bool = True) -> float:
    """
    Subtracts 2 numbers and returns the difference.

    :param num1: first number
    :param num2: second number
    :param in_order: order of subtraction. If True: num1 - num2 else: num2 - num1
    :return: difference of numbers
    """
    if in_order:
        return num1 - num2
    return num2 - num1


def multiply(num1: float, num2: float) -> float:
    """
    Multiples 2 numbers and returns the product

    :param num1: first number
    :param num2: second number
    :return: product of numbers
    """
    return num1 * num2


def divide(num1: float, num2: float, in_order: bool = True) -> float:
    """
    Divides 2 numbers and returns the quotient

    :param num1: first number
    :param num2: second number
    :param in_order: order of division. If True: num1 / num2 else: num2 / num1
    :return: quotient of division
    """
    if in_order:
        return num1 / num2
    return num2 / num1


def power(num: float, pwr: float) -> float:
    """
    Performs a power operation on a number
    :param num: base number
    :param pwr: exponent
    :return: resulting power of number
    """
    return num ** pwr
