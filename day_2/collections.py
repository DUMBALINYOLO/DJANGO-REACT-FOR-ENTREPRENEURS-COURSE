
# names = ["Sankwa", "Lapha", "Gaxa", 1, 2, 8]

# # names [2] = "Pa Gaxa"

# for name in names:
#     if name not in [1, 2, 8]:
#         print(f'String: {name}')
#         print("#####################################")
#     else:
#         print(f'Number: {name}')



# nums = [1, 20, 3, 5, 7]

# print(max(nums), " IS the largest number")


# max_num = nums[0]
# for number in nums:
#     if number > max_num:
#         max_num = number
# print(max_num)

# print("#####################################")

# min_num = nums[0]
# for number in nums:
#     if number < min_num:
#         min_num = number
# print(min_num)


# #2dimnsional lists


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# print(matrix[1][0])

# list methods


# nums = [50, 34, 67, 89, 90]
# print(nums)

# nums.append(909)
# print(nums)

# nums.insert(2, 13)
# print(nums)

# nums.clear()
# print(nums)

# nums.pop()
# print(nums)



# print(nums.count(2))
# nums.sort()
# nums.reverse()
# print(nums)



# numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]

# uniques = []

# for num in numbers:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)


# numbers1 = (1, 2, 7, 8, 9, 0)

# numbers1.append(100)




# storing information that comes as key value pairs

customer = {
    "name" : "Bash Aguero",
    "age" : 29,
    "purchase" : 500,
}

print(customer)
print(customer["age"])
customer["age"] = "Turning 50 in 21 years"
print(customer.get("age"))


nums = (1, 2, 5, 7, 8, 9, 10)
nums.append(789)



for num in nums:
    print(f'Num: {num}')














