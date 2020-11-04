
class Student:

	def __init__(self, name, mark, attendance=0):
		self.name = name
		self.mark = mark
		self.attendance = attendance

		
	
		
	def change_mark(self, score):
		self.mark = score
		return self.mark


	def set_attendance(self, present):
		self.attendance = present
		return self.attendance




justus = Student('Justus', 78)
# print(justus.mark)
mikael = Student('Mikael', 80)
# print(mikael.mark)

print(mikael.attendance)
mikael.set_attendance(190)
print(mikael.attendance)



# justus.change_mark(890)
# mikael.change_mark(900)

# print(mikael.mark)
# print(justus.mark)



