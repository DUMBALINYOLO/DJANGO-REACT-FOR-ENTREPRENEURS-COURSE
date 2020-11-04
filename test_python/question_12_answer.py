print('Enter "x" for exit!!!')
print('Tests were all out of 100')
print('Enter marks obtained in 5 subjects')
m1 = input()
if m1 == 'x':
	exit()
else:
	m2 = input()
	m3 = input()
	m4 = input()
	m5 = input()
	mark1 = int(m1)
	mark2 = int(m2)
	mark3 = int(m3)
	mark4 = int(m4)
	mark5 = int(m5)
	total = mark1 + mark2 + mark3 + mark4 + mark5
	average = total/5
	percentage = (total/500) * 100

	ranking = ''
	if percentage >= 60:
		ranking = 'Distinction'
		print(f'Your Average Mark is {average}')
		print(f'You got a {ranking}')
		print(f'You percentage is {percentage} %')
	elif percentage >= 45:
		ranking = 'Merit'
		print(f'Your Average Mark is {average}')
		print(f'You got a {ranking}')
		print(f'You percentage is {percentage} %')
	elif percentage >= 33:
		ranking = 'Pass'
		print(f'Your Average Mark is {average}')
		print(f'You got a {ranking}')
		print(f'You percentage is {percentage} %')
	else:
		ranking = 'Fail'
		print(f'Your Average Mark is {average}')
		print(f'You got a {ranking}')
		print(f'You percentage is {percentage} %')









