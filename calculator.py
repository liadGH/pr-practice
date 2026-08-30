def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    if b == 0:
        return 1
    if a == 0:
        if b > 0:
            return 0
        raise ZeroDivisionError("0.0 cannot be raised to a negative power")
    if a < 0 and not float(b).is_integer():
        raise ValueError("negative number cannot be raised to a fractional power")
    return a ** b
