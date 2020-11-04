

class Animal:

	def __init__(self, feet, tail, food):
		self.feet = feet
		self.food = food
		self.tail = tail

	def make_sound(self, sound):
		return sound


	def incr_feet(self):
		self.feet = self.feet * 10
		return self.feet



class Dog(Animal):

	def __init__(self, feet, tail, food, behavior):
		super().__init__(feet, tail, food)
		self.behavior = behavior


	


class Cat(Animal):

	pass


class Pig(Animal):

	def __init__(self, feet, tail, food, behavior):
		super().__init__(feet, tail, food)
		self.behavior = behavior



spingo = Dog(4, 'medium', 'anything', 'nasty')
# print(spingo.make_sound('Woof Woof'))
# print(spingo.incr_feet())

# print(spingo.__dict__)

print("*******************************")


lingo = Cat(7, 'SMALL', 'klllll')

print(lingo.__dict__)

print(help(lingo))


lula = Pig(4, 'small', 'anything even its kids', 'Its a Pig!!!, and its piggish')
# print(lula.make_sound('Oink Oink'))
# print(lula.__dict__)



