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

# Task 71.
