"""简易计算器模块（被测对象）"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("除法仅支持数值类型")
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b


def power(a, b):
    return a ** b


def mean(numbers):
    if not numbers:
        raise ValueError("数据列表不能为空")
    return sum(numbers) / len(numbers)
