

# applies a given function to all iterables and returns a new ist


li = [10, 20, 30, 40, 50, 60, 70, 80, 90]

newli = list(map(lambda a:(a**2), li))

print(newli)


from functools import reduce

a = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])

print(a)


lang = [1, 2, 3,4, 5, 6, 7, 8,9]
ch2008 = list(filter(lambda a:(a/a==1), lang))
print(ch2008)
