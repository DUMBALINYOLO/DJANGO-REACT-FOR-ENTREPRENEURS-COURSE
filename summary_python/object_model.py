

class Polynomial:
	
	def __init__(self, *coefs):
		self.coefs = coefs

	def __repr__(self):
		return f'Polynomial(*{self.coefs})'

	def __add__(self, other):
		return Polynomial(*(x + y for x, y in zip(self.coefs, other.coefs)))
 
	def __len__(self):
		return len(self.coefs)

	def __call__(self):
		pass
		


p1 = Polynomial(10, 90, 90)
p2 = Polynomial(20, 190, 190)

print(p1)
print(p2 + p1)


