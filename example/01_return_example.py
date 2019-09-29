# coding=utf-8
def plus(val1, val2):
	return val1 + val2


def minus(val1, val2):
	return val1 - val2


def multiple(val1, val2):
	return val1 * val2


def divide(val1, val2):
	return val1 / val2


result_plus = plus(10, 20)
result_minus = minus(10, 20)
result_multiple = multiple(10, 20)
result_divide = divide(10, 20)

print("plus", result_plus)
print("minus", result_minus)
print("multiple", result_multiple)
print("divide", result_divide)

# 10 - 20한 결과에 50 * 10 한 결과를 / 나누어라
print("calculate", divide(plus(10, 20), multiple(50, 10)))
print(-10 / 500)
temp = -10.00 / 500.00
print(type(temp), temp)
