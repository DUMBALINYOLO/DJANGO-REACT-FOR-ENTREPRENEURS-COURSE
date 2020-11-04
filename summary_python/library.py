
class BaseMeta(type):
	"""docstring for BaseMeta"""

	def __new__(cls, name, bases, body):
		if not 'bar' in body:
			raise TypeError('Bad User Class')
		return super().__new__(cls, name, bases, body)
	
	


class Base(metaclass=BaseMeta):
	"""docstring for Base"""
	def foo(self):
		return 'foo'

	def __init_subclass__(cls, *args, **kwargs):
		return super().__init_subclass__(*args, **kwargs)


		