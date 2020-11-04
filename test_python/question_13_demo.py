
i = 1
while True:
	print('Please enter your temperature')
	temperature = int(input())
	if temperature >= 100:
		print('It is hot')
	elif temperature > 60:
		print('It is a nice day')
	elif temperature > i:
		print('It is cold')
	else:
		break