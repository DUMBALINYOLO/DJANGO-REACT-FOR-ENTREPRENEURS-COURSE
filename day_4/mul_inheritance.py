
class Father:
	"""docstring for Father"""
	def __init__(self, calm, brains, surname):
		self.calm = calm
		self.brains = brains


class Mother:
	"""docstring for Father"""
	def __init__(self, speak, annoying):
		self.speak = speak
		self.annoying = annoying


class Child(Father, Mother):

	def __init__(self, calm, brains, surname, speak, annoying, trust):
		Father.__init__(self, calm, brains, surname)
		Mother.__init__(self, speak, annoying)
		self.trust = trust



xylem = Child(
			'Yes Calm', 
			'Yes a lot',
			'Moyo',
			'Too Much',
			'Well yes',
			'Not Trust worth'
		)
print(xylem.__dict__)







			
						