

for i in range(10 + 12):
    print(i)

maxola = "Dumbalinyolo"

for umudwa in maxola:
    print(umudwa)
    print("Utsintso")


num = int(input("Number"))
factorial = 1

if num < 0:
    print("Num must be positive")
elif num == 0:
    print("Factoial is equal to 1")
else:
    for i in range(1, num * 1):
        factorial = factorial * (i + 1)
print(factorial)




# Guessing Game

num = 8
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == num:
        print("You win fucker")
        break
else:
    print("Its your loss")


import random

to_be_guessed = random.randint(1, 10)
guess = 0

while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that your are giving up")
        break
else:
    print("Congratulations you win")


prices = [10, 20, 30]

total = 0
symbol = "$"

for price in prices:
	total += price
print(f"Total: {symbol}{total}")






