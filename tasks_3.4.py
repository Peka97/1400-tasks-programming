# Tasks 3.4
#
# # Task 63.
# array = []
# while True:
# 	num = int(input("Enter num (0 for QUIT): "))
# 	if num == 0:
# 		print(sum(array))
# 		break
# 	else:
# 		array.append(num)
#
# # Task 64.
# result = []
# prices = [4.95, 9.95, 14.95, 19.95, 24.95]
# sale = 0.6
# for price in prices:
# 	result.append([price, sale, round(price*sale, 2)])
# for row in result:
# 	print(row)
#
# # Task 65.
# result = [["Цельсий", "Фаренгейт"]]
# for num in range(10, 101, 10):
# 	result.append([num, int(num*1.8+32)])
# for row in result:
# 	print(row)

# # Task 66.
# import math
#
# PENNIES = 5
# NICKEL = 0.05
# total = 0.00
# line = input("Enter your price(empty string to QUIT): ")
#
# while line != '':
# 	total += float(line)
# 	line = input("Enter your price(empty string to QUIT): ")
#
# print("Total price: %.02f" % total)
#
# rounding_indicator = total * 100 % PENNIES
# if rounding_indicator < PENNIES / 2:
# 	cash_total = total - rounding_indicator / 100
# else:
# 	cash_total = total + rounding_indicator / 100
#
# print('Total cash price: %.02f' % cash_total)

# # Task 67.
# from math import sqrt
# coords = []
# while True:
# 	x_y = input("Enter 'X Y' coord-s or QUIT: ")
# 	if x_y != 'QUIT':
# 		coords.append([int(x_y.split()[0]), int(x_y.split()[1])])
# 	else:
# 		break
# print(coords)
# result = 0
# for x in range(0, len(coords), 2):
# 	print(x)
# 	x1 = coords[x][0]
# 	y1 = coords[x][1]
# 	x2 = coords[x+1][0]
# 	y2 = coords[x+1][1]
# 	perimetr = sqrt((x2 - x1)**2 + (y2 - y1)**2)
# 	result += perimetr
# print(result)

# # Task 68.
# grades = {
# 	'A+': 4.3,
# 	'A': 4.0,
# 	'A-': 3.7,
# 	'B+': 3.3,
# 	'B': 3.0,
# 	'B-': 2.7,
# 	'C+': 2.3,
# 	'C': 2.0,
# 	'C-': 1.7,
# 	'D+': 1.3,
# 	'D': 1.0,
# 	'D-': 0
# }
# result = []
# while True:
# 	enter = input("Enter your grade: ")
# 	if enter != "":
# 		for grade, val in grades.items():
# 			if enter == grade:
# 				result.append(val)
# 				break
# 			elif val == 0:
# 				print("Invalid grade")
# 	else:
# 		break
# print(sum(result))

# # Task 69.
# total = 0.00
# while True:
# 	age = input("Enter your age of space to QUIT: ")
# 	if age == '':
# 		break
# 	else:
# 		age = int(age)
# 		if 3 <= age <= 12:
# 			total += 14.00
# 		elif age >= 65:
# 			total += 18.00
# 		else:
# 			total += 23.00
# print("$%.02f" % total)

# # Task 70.
# while True:
# 	bit = input("Enter 8 bit or space to QUIT: ")
# 	if len(bit) != 8:
# 		print('Invalid enter')
# 	else:
# 		ones = bit.count('1')
# 		if ones % 2 == 0:
# 			print(0)
# 		else:
# 			print(1)

# Task 71. Skip

# # Task 72.
# for num in range(1, 101):
# 	print(num)
# 	enter = input("What you say? (F)izz, (B)uzz, (FB) or (N)one?\n>: ")
# 	if num % 3 == 0 and enter == "F":
# 		continue
# 	elif num % 5 == 0 and enter == "B":
# 		continue
# 	elif num % 3 == 0 and num % 5 == 0 and enter == "FB":
# 		continue
# 	else:
# 		if enter == "N":
# 			continue
# 		else:
# 			print("You lose!")
# 			break
# print("You win!!!")

# # Task 73.
# text = input("Enter text: ")
# x = int(input("Enter num: "))
# result = ''
# for letter in text:
# 	result += chr(ord(letter) - x)
# print(result)

# # Task 74. Skip
# from numpy import mean
#
# x = int(input("Enter x: "))
# guess = x / 2
# while str(guess)[-1] != "0":
# 	guess = mean([guess, x / guess])
# print(guess)

# # Task 75.
# word = input("Enter word: ")
# x = 0
# y = -1
# pallindrome = True
# if len(word) % 2 == 0:
# 	for _ in range(int(len(word)/2)):
# 		if word[x] == word[y]:
# 			x += 1
# 			y -= 1
# 		else:
# 			pallindrome = False
# 			break
# else:
# 	for _ in range(int((len(word)/2)-1)):
# 		if word[x] == word[y]:
# 			x += 1
# 			y -= 1
# 		else:
# 			pallindrome = False
# 			break
# print(f"{word} is pallindrome") if pallindrome is True else print(f"{word} is not pallindrome")

# # Task 76.
# text = input("Enter text: ")
# sample = text.replace(' ', '')
# x = 0
# y = -1
# palindrome = True
# if len(sample) % 2 == 0:
# 	for _ in range(int(len(sample)/2)):
# 		if sample[x] == sample[y]:
# 			x += 1
# 			y -= 1
# 		else:
# 			palindrome = False
# 			break
# else:
# 	for _ in range(int((len(sample)/2)-1)):
# 		if sample[x] == sample[y]:
# 			x += 1
# 			y -= 1
# 		else:
# 			palindrome = False
# 			break
# print(f"{text} is palindrome") if palindrome is True else print(f"{text} is not palindrome")

# # Task 77.
# matrix = [
# 	[1, ],
# 	[2, ],
# 	[3, ],
# 	[4, ],
# 	[5, ],
# 	[6, ],
# 	[7, ],
# 	[8, ],
# 	[9, ],
# 	[10, ]
# ]
# for row in range(0, 10):  # Формирую
# 	for x in range(1, 11):
# 		matrix[row].append(x * matrix[row][0])
# for row in range(len(matrix)):  # Форматирую
# 	for x in range(len(matrix[row])):
# 		if len(str(matrix[row][x])) == 1:
# 			matrix[row][x] = f'0{matrix[row][x]}'
# matrix[0][0] = '  '
# for row in matrix:  # Вывожу
# 	print(*row)

# # Task 78.
# import math
#
# enter = int(input("Enter positive num: "))
# lst = [enter, ]
# while lst[-1] != 1:
# 	if lst[-1] % 2 == 0:
# 		lst.append(math.ceil(lst[-1]/2))
# 	else:
# 		lst.append(lst[-1]*3+1)
# print(lst)

# # Task 79.
# m = int(input("Enter m: "))
# n = int(input("Enter n: "))
# d = m if m > n else n
# while n % d != 0 or m % d != 0:
# 	d -= 1
# print(d)

# # Task 80.
# from math import ceil
# n = int(input("Enter n (2 or more): "))
# result = []
# factor = 2
# while factor <= n:
# 	if n % factor == 0:
# 		result.append(factor)
# 		n = ceil(n / factor)
# 	else:
# 		factor += 1
# print(result)

# # Task 81.
# enter = input("Enter num: ")
# print(int(enter, 2))
#
# # Task 82.
# enter = int(input("Enter num: "))
# print(bin(enter))

# # Task 83.
# import random
# array = [random.randint(1, 100) for _ in range(0, 101)]
# max_array = 0
# count = 0
# for x in array:
# 	if x > max_array:
# 		max_array = x
# 		count += 1
# 		print(x, "<== Обновление")
# 	else:
# 		print(x)
# print(f"Максимальное число: {max_array}\nКоличество смен: {count}")

# # Task 84.
# from random import randint
# count = 0
# lst = [0, 0, 0]
# while lst[-1:-4:-1] != [1, 1, 1]:
# 	lst.append(randint(0, 1))
# 	count += 1
# print(lst[3:])
# print(count)
