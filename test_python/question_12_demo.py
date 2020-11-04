print('Enter "x" for exit')
print('Your tests were all out of 100')
print('Enter marks which were attained in 5 subjects')

m1 = input()
if m1 == 'x':
	exit()
else:
	m2 = input()
	m3 = input()
	m4 = input()
	m5 = input()
	mark1 = int(m1)
	mark2= int(m2)
	mark3 = int(m3)
	mark4 = int(m4)
	mark5 = int(m5)
	total_mark = mark1 + mark2 + mark3 + mark4
	average = total_mark / 5
	percentage = (total_mark/500) * 100

	ranking = ''
	if percentage >= 60:
		ranking = 'Distinction'
		print(f'Your average mark is {average}')
		print(f'Your Percentage is {percentage} %')
		print(f'Your ranking is {ranking}')
	elif percentage >= 45:
		ranking = 'Merit'
		print(f'Your average mark is {average}')
		print(f'Your Percentage is {percentage} %')
		print(f'Your ranking is {ranking}')
	elif percentage >= 33:
		ranking = 'Pass'
		print(f'Your average mark is {average}')
		print(f'Your Percentage is {percentage} %')
		print(f'Your ranking is {ranking}')
	else:
		ranking = 'Fail'
		print(f'Your average mark is {average}')
		print(f'Your Percentage is {percentage} %')
		print(f'Your ranking is {ranking}')














