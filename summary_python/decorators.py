from functools import wraps

def debug(func):
	# func is a function being wrapped
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(func.__qualname__)
		return func(*args, **kwargs)
	return wrapper



@debug
def add(x, y):
	return x + y

@debug
def subtract(x, y):
	return x - y

@debug
def multiply(x, y):
	return x * y
@debug
def divide(x, y):
	return x / y
@debug
def power(x, y):
	return x ** y


print(add(10, 90))

print(subtract(10, 90))

print(multiply(10, 90))

print(divide(10, 90))

print(power(10, 90))


print(help(debug))





