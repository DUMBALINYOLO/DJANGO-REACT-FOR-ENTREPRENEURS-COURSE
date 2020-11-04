from functools import wraps, partial

def debug(func=None, *, prefix=''):
	# func is a function being wrapped
	if func is None:
		return partial(debug, prefix=prefix)
		
	msg = prefix + func.__qualname__
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(msg)
		return func(*args, **kwargs)
	return wrapper




@debug(prefix='+++')
def add(x, y):
	return x + y

@debug(prefix='---')
def subtract(x, y):
	return x - y

@debug(prefix='***')
def multiply(x, y):
	return x * y


@debug(prefix='///')
def divide(x, y):
	return x / y

@debug(prefix='^^^')
def power(x, y):
	return x ** y




print(add(10, 90))

print(subtract(10, 90))

print(multiply(10, 90))

print(divide(10, 90))

print(power(10, 90))

