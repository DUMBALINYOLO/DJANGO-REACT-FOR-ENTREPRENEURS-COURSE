from collections import OrderedDict

class Driver:

	def __init__(self, name, sex, qualification, score):
		
		self.name = name
		self.sex =sex
		self.qualification = qualification
		self.score = score

	def __str__(self):
		
		return f'Name: {self.name}, Gender: {self.sex}, Qualification: {self.qualification}, Score: {self.score}'







abidal = Driver('Abidal', 'Male', 'Class A', 90)
anyijesu = Driver('Abidal', 'Male', 'Class A', 90)
justus = Driver('Abidal', 'Male', 'Class A', 90)
mikal = Driver('Abidal', 'Male', 'Class A', 90)
bash = Driver('Abidal', 'Male', 'Class A', 90)
otorugu = Driver('Abidal', 'Male', 'Class A', 90)
azi = Driver('Abidal', 'Male', 'Class A', 90)
makhail = Driver('Abidal', 'Male', 'Class A', 90)
obinwa = Driver('Obinwa', 'Male', 'Class A', 90)
ikwa = Driver('Ikwa', 'Female', 'Class A', 90)


# print(abidal.__dict__)
# print(anyijesu.__dict__)
# print(justus.__dict__)
# print(mikal.__dict__)
# print(bash.__dict__)
# print(otorugu.__dict__)
# print(azi.__dict__)
# print(makhail.__dict__)
# print(obinwa.__dict__)
# print(ikwa.__dict__)


print(abidal)
print(anyijesu)
print(justus)
print(mikal)
print(bash)
print(otorugu)
print(azi)
print(makhail)
print(obinwa)
print(ikwa)


print(help(Driver))

print(help(OrderedDict))

