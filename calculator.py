"""简易计算器模块（被测对象）"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b


def power(a, b):
    return a ** b


def mean(numbers):
    if not numbers:
        raise ValueError("数据列表不能为空")
    return sum(numbers) / len(numbers)
