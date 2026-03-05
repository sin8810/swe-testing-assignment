from calculator import Calculator

calc = Calculator()

def calculate(a, operator, b):

    if operator == "+":
        return calc.add(a, b)

    elif operator == "-":
        return calc.subtract(a, b)

    elif operator == "*":
        return calc.multiply(a, b)

    elif operator == "/":
        return calc.divide(a, b)

    else:
        raise ValueError("Invalid operator")