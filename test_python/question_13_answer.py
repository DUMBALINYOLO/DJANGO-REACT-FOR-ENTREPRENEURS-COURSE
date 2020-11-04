

i = 1
print('Please Enter your Temperature')
while True:
	temperature = int(input())
	if temperature > 100:
		print('Its too hot go swimming')
	elif temperature > 60:
		print('Its cool temperature')
	elif temperature >= 1:
		print('Its too cold')
	else:
		break

