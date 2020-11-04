from inspect import getsource
from time import time


def timer(func, x, y):


def add(x, y=10):
	return y + y

print(add.__qualname__)
print(add.__defaults__)
print(add.__module__)
print(add.__code__.co_code)
print(add.__code__.co_nlocals)
print(add.__code__.co_varnames)
print(getsource(add))