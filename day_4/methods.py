class Student:

	def __init__(self, name, mark):
		self.name = name
		self.mark = mark
		
	
		
	def change_mark(self, score):
		self.mark = score
		return self.mark



justus = Student('Justus', 78)
justus.change_mark(990)
print(justus.mark)

