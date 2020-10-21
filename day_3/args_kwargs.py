
def args_kwargs(*args, **kwargs):
	# *args stands for positional arguments and * meaning as many as you can pass
	# **kwargs means key words arguments and ** is for passing as many as you like
	# args can be any datatype you want to pass
	# kwargs have got an asignment operator like a varible for they point to smtn
	print(args, kwargs)
	print(kwargs)


args_kwargs(
	# *args
	'Math', 
	'Geo', 
	'Sci',
	'Pysh',
	'Quanta',
	# **kwargs
	n='English',
	z='Bio',
	a= 'Kwasa',
	d= 'Zamula'
)


def fullname(name, surname):
	return f'My name is {name}, and my surname is {surname}'


print(fullname(surname='Okechi', name='Justus'))
	

def zargs_kwargs(*subjects, **languages):
	print(subjects, languages)
	print(languages)


# zargs_kwargs(
# 	'Math', 
# 	'Geo', 
# 	'Sci',
# 	# l='lkklll',
# 	'Pysh',
# 	'Quanta',
# 	n='English',
# 	z='Bio',
# 	a= 'Kwasa',
# 	d= 'Zamula'
# )
