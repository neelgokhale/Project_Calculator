"""
Created by Neel Gokhale at 2020-07-19
File calculator.py from project Project_Calculator
Built using PyCharm

"""

import functions as f

run = True
print("___Python Calculator___")

while run:

    num1 = float(input("> Please enter the first number: "))
    num2 = float(input("> Please enter the second number: "))

    print(
        """
        The following arithmetic operators can be used:
        - For addition, press A
        - For subtraction, press S
        - For multiplications, press M
        - For division, press D
        - To quit, press X
        """
    )

    op = input("> Enter operator key: ").lower()

    if op == 'x':
        break

    elif op == 'a':
        print("> The answer is: ", f.add(num1, num2))

    elif op == 's':
        in_order = bool(int(input(">> Enter 1 -> num1 - num2 OR Enter 0 -> num2 - num1: ")))
        print("> The answer is: ", f.subtract(num1, num2, in_order=in_order))

    elif op == 'm':
        print("> The answer is: ", f.multiply(num1, num2))

    elif op == 'd':
        in_order = bool(int(input(">> Enter 1 -> num1 / num2 OR Enter 0 -> num2 / num1")))
        print("> The answer is: ", f.divide(num1, num2, in_order=in_order))

    else:
        print("> Invalid entry, try again...")
