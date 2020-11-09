
class Vehicle:

	def __init__(self, name, model):
		self.name = name
		self.model = model

	def honk(self):
		pass




class Car(Vehicle):

	def __init__(self, speed):
		super().__init__(name, model)
		self.speed = speed


	def honk(self):
		print('Wong Wong Wong')


class WheelBarrow(Vehicle):

	def __init__(self, noise):
		super().__init__(name, model)
		self.noise = self.noise

	def honk(self):
		print('Kwak kwak kwak zak')


print(help(WheelBarrow))


