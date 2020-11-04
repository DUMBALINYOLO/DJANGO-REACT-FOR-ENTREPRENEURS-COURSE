
class Student:

	def __init__(self, mark, attendance):
		self.mark = mark
		self.attendance = attendance


	def __add__(self, other):
		return Student(self.mark + other.mark, self.attendance + other.attendance)

	def __mul__(self, other):
		return Student(self.mark * other.mark, self.attendance * other.attendance)

	def __sub__(self, other):
		return Student(self.mark - other.mark, self.attendance - other.attendance)

	def __pow__(self, other):
		return Student(self.mark ** other.mark, self.attendance ** other.attendance)


	def __gt__(self, other):
		return self.mark > other.mark

	def __ge__(self, other):
		return self.mark >= other.mark

	def __lt__(self, other):
		return self.mark < other.mark

	def __le__(self, other):
		return self.mark <= other.mark

	def __eq__(self, other):
		return self.mark == other.mark


	def __str__(self):
		return f' Mark: {self.mark}, Attendance: {self.attendance}'


xola = Student(89, 50)	
xyl = Student(90, 55)
almus = Student(86, 60)	
kwamul = Student(69, 60)

print(xola > xyl)
print(xola > almus)
print(xola > kwamul)
print(xyl > almus)
print(xyl > kwamul)





