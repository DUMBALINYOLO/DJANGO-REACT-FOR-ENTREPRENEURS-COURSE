
class Student:

	def __init__(self, name, mark, att):
		self.name = name
		self.mark = mark
		self.att = att

	def change_mark(self, incr):
		self.mark = self.mark + incr
		return self.mark

	def change_att(self, dcr):
		self.att = self.att - dcr
		return self.att

	def __str__(self):
		return f'NAME: {self.name}, MARK: {self.mark}, Attendance: {self.att}'



justus = Student('Justus', 98, 67)
michael = Student('Michael', 97, 68)

print('Before calling a method')

print(justus)
print(michael)

print("After calling a change method")

justus.change_mark(78)
michael.change_mark(89)
print(justus)
print(michael)

print("aFTER CHANGING THE Attendance")

justus.change_att(10)
michael.change_att(18)

print(justus)
print(michael)












		




		