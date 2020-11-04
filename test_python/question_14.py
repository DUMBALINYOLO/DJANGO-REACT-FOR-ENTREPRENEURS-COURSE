
for number in range(100):
	if number % 5 == 0 and number % 3 == 0:
		print(f'{number} is fizz-buzz')
	elif number % 3 == 0:
		print(f'{number} if fizz')
	elif number % 5 == 0:
		print(f'{number} is buzz')
	else:
		print(f'{number} does not belong to a fizz-buzz fandom')

