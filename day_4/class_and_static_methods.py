
class Dog:

	dogs = []


	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		self.dogs.append(self)


	@classmethod
	def num_dogs(cls):
		return len(cls.dogs)

	@staticmethod
	def bark(n):
		for _ in range(n):
			print('Woof Woof !!!!')

	def __str__(self):
		return self.name


sport = Dog('Sport')
boss = Dog('Boss')
lion = Dog('Lion')
timer = Dog('Timer')
thula = Dog('Thula')

n = Dog.num_dogs()
print(Dog.bark(Dog.num_dogs()))





		