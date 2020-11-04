from library import Base



class Derived(Base):
	"""docstring for Derived"""
	
	def bar(self):
		return self.foo()




print(help(Derived))