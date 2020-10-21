class Car:

	def __init__(self, wheels, model, engine):
		self.wheels = wheels
		self.model = model
		self.engine = engine
		print('I am quite special dude')




bmw = Car(4, '5 SERIES', 'H7GHB0')
toyota = Car(4, 'SKHUMBA', '2700I')
benz = Car(4, 'STELLAR', 'H7GLLL')

print(bmw.__dict__)
print(toyota.__dict__)
print(benz.__dict__)
