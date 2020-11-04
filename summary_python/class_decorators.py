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



def debugmethods(cls):
	for key, val in vars(cls).items():
		if callable(val):
			setattr(cls, key, debug(val))

	return cls



@debugmethods
class Spam(object):
	"""docstring for Spam"""
	def a(self):
		pass


	def b(self):
		pass


	def c(self):
		pass


s = Spam()


s.a()
s.b()
s.c()

