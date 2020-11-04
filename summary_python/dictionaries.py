# capitals = dict()

# capitals['zimbabwe'] = 'Harare'
# capitals['South Africa'] = 'Pretoria'
# capitals['Botswana'] = 'Gaborone'
# capitals['zambia'] = 'lusaka'

# countries = ['zimbabwe', 'South Africa', 'Botswana', 'zambia']

# for country in countries:
# 	if country in capitals:
# 		print(f'The capital of {country} is {capitals[country]}')
# 	else:
# 		print(f'The capital of {country} is none')


# counter = {}
# for word in input().split():
# 	counter[word] = counter.get(word, 0) + 1
# 	# print(counter[word] + 1, end = ' ')


# n = int(input())
# d = {}
# for i in range(n):
# 	first, second = input().split()
# 	d[first] = second
# 	d[second] = first
# print(d[input()])


# def mult_iter(a, b):
# 	result = 0
# 	while b > 0:
# 		result += a
# 		b -= 1
# 	return result

# print(mult_iter(2, 2))

# def mult(a, b):
# 	if b == 1:
# 		return a
# 	else:
# 		return a + mult(a, b-1)

# print(mult(10, 10))

# def fact(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * fact(n-1)

# print(fact(400))

# def print_move(fr, to):
# 	print(f'move from {fr} to {to}')


# def towers(n, fr, to, spare):
# 	if n == 1:
# 		print_move(fr, to)
# 	else:
# 		towers(n-1, fr, spare, to)
# 		towers(1, fr, to, spare)
# 		towers(n-1, spare, to, fr)

# print(towers(5, 'ka', 'da', 'me'))


# def fib(x):
# 	if x == 0 or x == 1:
# 		return 1
# 	else:
# 		return fib(x-1) + (x-2)


# print(fib(5))


# def is_palindrome(s):
	
# 	def to_chars(s):
# 		s = s.lower()
# 		ans = ''
# 		for c in s:
# 			if c in 'abcdefghijklmnopqrstuvwxyz':
# 				ans = ans + c
# 		return ans

# 	def is_pal(s):
# 		if len(s) <= 1:
# 			return True
# 		else:
# 			return s[0] == s[-1] and is_pal(s[1:-1])
# 	return is_pal(to_chars(s))

# print(is_palindrome('zyxwvutsrqponmlkjihgfedcba'))


# my_dict = {}

# grades = {'Anna': 'B', 'JOHN': 'A', 'ISA':'C'}

# grades['alms'] = 'B'
# grades['max'] = 'F'

def lyrics_to_frequencies(lyrics):
	my_dict = {}
	for word in lyrics:
		if word in my_dict:
			my_dict[word] += 1
		else:
			my_dict[word] = 1
	return my_dict

ukufa = [
			'ukufa',
			'lasa',
			'suma',
			'yama',
			'suma',
			'lasa',
			'lasa',
			'ukufa',
			'sengaze',
			'abantwa',
			'la',
			'la',
			'lasa',
			'toro',
			'saka',
			'toro',
			'jozo',
			'jozo',
			'kala',
			'suma'
		]


print(lyrics_to_frequencies(ukufa))




























