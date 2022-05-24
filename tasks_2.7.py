# Tasks 2.7

# Task 35.
num = int(input("Enter num: "))
print("чет") if num % 2 == 0 else print("нечет")

# Task 36.
dog_age = int(input("Enter age of dog: "))
if dog_age <= 2:
	print(f"Your dog {dog_age * 10.5} years old")
else:
	print(f"Your dog {dog_age * 4} years old")

# Task 37.
letter = input("Enter letter: ")
if letter in ["a", "e", "i", "o", "u"]:
	print("Letter is vowel")
else:
	print("Letter is consonant")

# Task 38.
count_of_side = int(input("Enter count of side your figure: "))
if count_of_side == 3:
	print("That's Triangle!")
elif count_of_side == 4:
	print("That's Square!")
elif count_of_side == 5:
	print("That's Pentagon!")
elif count_of_side == 6:
	print("That's Geptagon!")
elif count_of_side == 7:
	print("That's Gexagon!")

# Task 39.
month = input("Enter month: ")
if month in ["January", "March", "May", "July", "August", "October", "December"]:
	print("In this month 31 days")
elif month in ["April", "June", "September", "November"]:
	print("In this month 30 days")
else:
	print("In this month 28 or 29 days")

# Task 40.
volume = int(input("Enter volume level: "))
jackhummer = 130
lawn_mover = 106
alarm = 70
quiet_room = 40
if volume > jackhummer:
	print("So much")
elif volume == jackhummer:
	print("That's Jackhammer")
elif lawn_mover < volume < jackhummer:
	print("Between Lawn mover and Jackhammer")
elif volume == lawn_mover:
	print("That's Lawn mover")
elif alarm < volume < lawn_mover:
	print("Between Alarm and Lawn mover")
elif volume == alarm:
	print("That's Alarm")
elif quiet_room < volume < alarm:
	print("Between Quiet room and Alarm")
elif volume == quiet_room:
	print("That's Quiet Room")
elif volume < quiet_room:
	print("So less")

# Task 41.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a == b == c:
	print("Equilateral Triangle")
elif a == b or b == c or a == c:
	print("Isosceles Triangle")
else:
	print("Versatile Triangle")

# Task 42.
note = input("Enter note: ")
oct = note[0]
num = int(note[1])
oct_dict = {"C": 261.63, "D": 293.66, "E": 329.63, "F": 349.23, "G": 392.00, "A": 440.00, "B": 493.88}
db = 0
if oct_dict.get(oct):
	db = oct_dict.get(oct)
	if num < 4:
		for _ in range(num, 4):
			db *= 0.5
	elif num > 4:
		for _ in range(4, num):
			db *= 2
	print(db)
else:
	print("Invalid input")

# Task 43.
db = float(input("Enter dB: "))
oct_dict = {"C": 261.63, "D": 293.66, "E": 329.63, "F": 349.23, "G": 392.00, "A": 440.00, "B": 493.88}
for note, val in oct_dict.items():
	if val - 1 < db < val + 1:
		print(f"{note}4")

# Task 44.
dollars = {
	1: "Джордж Вашингтон",
	2: "Томас Джефферсон",
	5: "Авраам Линкольн",
	10: "Александр Гамильтон",
	20: "Эндрю Джексон",
	50: "Улисс Грант",
	100: "Бенджамин Франклин"
}
denomination = int(input("Enter denomination: "))
for den, name in dollars.items():
	if den == denomination:
		print(name)

# Task 45.
dates = {
	"New Year": "1 January",
	"Day of Canada": "1 July",
	"Christmas": "25 December"
}
enter = input("Enter date: ")
for holiday, date in dates.items():
	if date == enter:
		print(holiday)

# Task 47.
enter = input("Enter coordinates: ")
if enter[0] in ["a", "c", "e", "g"]:
	if int(enter[1]) % 2 != 0:
		print("Black")
	else:
		print("White")
else:
	if int(enter[1]) % 2 == 0:
		print("Black")
	else:
		print("White")

# Task 48.
zodiacs = {
	"Козерог": [[range(22, 31 + 1), "December"], [range(1, 19 + 1), "January"]],
	"Водолей": [[range(20 + 1, 31 + 1), "January"], [range(1, 18 + 1), "February"]],
	"Рыбы": [[range(19, 28 + 1), "February"], [range(1, 20 + 1), "March"]],
	"Овен": [[range(21, 31 + 1), "March"], [range(1, 19 + 1), "April"]],
	"Телец": [[range(20, 30 + 1), "April"], [range(1, 20 + 1), "May"]],
	"Близнецы": [[range(21, 31 + 1), "May"], [range(1, 20 + 1), "June"]],
	"Рак": [[range(21, 30 + 1), "June"], [range(1, 22 + 1), "July"]],
	"Лев": [[range(23, 31 + 1), "July"], [range(1, 22 + 1), "August"]],
	"Дева": [[range(23, 31 + 1), "August"], [range(1, 22 + 1), "September"]],
	"Весы": [[range(23, 30 + 1), "September"], [range(1, 22 + 1), "October"]],
	"Скорпион": [[range(23, 31), "October"], [range(1, 21 + 1), "November"]],
	"Стрелец": [[range(22, 30 + 1), "November"], [range(1, 21 + 1), "December"]]
}
enter = input("Enter your burn date: ")
num = enter.split()[0]
month = enter.split()[1]
for zodiac, dates in zodiacs.items():
	if (int(num) in dates[0][0] or int(num) in dates[1][0]) and (dates[0][1] == month or dates[1][1] == month):
		print(zodiac)
		break

# Task 49.
y = int(input("Enter your burn year: "))
china_horoscope = {
	2000: "Дракон",
	2001: "Змея",
	2002: "Лошадь",
	2003: "Коза",
	2004: "Обезьяна",
	2005: "Петух",
	2006: "Собака",
	2007: "Свинья",
	2008: "Крыса",
	2009: "Бык",
	2010: "Тигр",
	2011: "Кролик"
}
x = 0
if y >= 2000:
	while True:
		for year, animal in china_horoscope.items():
			if y == year + x:
				print(animal)
				break
		x += 12
else:
	while True:
		for year, animal in china_horoscope.items():
			if y == year - x:
				print(animal)
				break
		x += 12

# Task 50.
richter_scale = {
	"Minimum": range(2 + 1),
	"Very weak": range(2, 3 + 1),
	"Weak": range(3, 4 + 1),
	"Intermediate": range(4, 5 + 1),
	"Medium": range(5, 6 + 1),
	"Strong": range(6, 7 + 1),
	"Very strong": range(7, 8 + 1),
	"Large": range(8, 9 + 1),
	"Destructive": range(10, )
}
magnitude = int(input("Enter magnitude: "))
for name, val in richter_scale.items():
	if magnitude in val:
		print(name)
		break

# Task 51. Skip, don't understand
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Task 52.
grades = {
	'A+': 4.3,
	'A': 4.0,
	'A-': 3.7,
	'B+': 3.3,
	'B': 3.0,
	'B-': 2.7,
	'C+': 2.3,
	'C': 2.0,
	'C-': 1.7,
	'D+': 1.3,
	'D': 1.0,
	'D-': 0
}
enter = input("Enter your grade: ")
for grade, val in grades.items():
	if enter == grade:
		print(val)
		break
	print("Invalid grade")

# Task 53.
grades = {
	'A+': 4.3,
	'A': 4.0,
	'A-': 3.7,
	'B+': 3.3,
	'B': 3.0,
	'B-': 2.7,
	'C+': 2.3,
	'C': 2.0,
	'C-': 1.7,
	'D+': 1.3,
	'D': 1.0,
	'D-': 0
}
enter = float(input("Enter your grade: "))
for grade, val in grades.items():
	if enter == val:
		print(grade)
		break
	print("Invalid grade")

# Task 54.
enter = float(input("Enter your grade: "))
rating = {0: "Low", 4: "Medium", 0.6: "High"}
for rate, name in rating.items():
	if enter == rate:
		print(f"Scale: {2400.00 * rate}$")
	elif enter > 0.6:
		print(f"Scale: {2400.00 * enter}$")

# Task 55.
dict_len = {
	'Фиолетовый': range(380, 450),
	'Синий': range(450, 495),
	'Зеленый': range(495, 570),
	'Желтый': range(570, 590),
	'Оранжевый': range(590, 620),
	'Красный': range(620, 750)
}
enter = int(input("Enter length of wave: "))
for name, length in dict_len.items():
	if enter in length:
		print(name)
		break
else:
	print("Invalid length")

# Task 56.
dict_range = {
	"Радиоволны": range(0, 3 * 10 ** 9),
	"Микроволны": range(3 * 10 ** 9, 3 * 10 ** 12),
	"Инфракрасное излучение": range(3 * 10 ** 12, 43 * 10 ** 13),
	"Видимое излучение": range(43 * 10 ** 13, 75 * 10 ** 13),
	"Ультрафиолетовое излучение": range(75 * 10 ** 13, 3 * 10 ** 17),
	"Рентгеновское излучение": range(3 * 10 ** 17, 3 * 10 ** 19),
	"Гамма-излучение": range(3 * 10 ** 19, )
}
enter = int(input("Enter Frequency: "))
enter = enter * 10 ** 12
for name, val in dict_range.items():
	if enter in val:
		print(name)
		break
else:
	print("Invlid frequency")

# Task 57.
minutes = int(input("Enter minutes: "))
sms = int(input("Enter count of sms: "))
total_price = 15
print(total_price)
if minutes > 50:
	total_price += (minutes - 50) * 0.25
if sms > 50:
	total_price += (sms - 50) * 0.15
total_price += 0.44
total_price *= 1.05
print(round(total_price, 2))

# Task 58.
year = int(input("Enter year: "))
if year % 400 == 0:
	print("Високосный")
else:
	if year % 100 == 0:
		print("Не високосный")
	else:
		if year % 4 == 0:
			print("Високосный")
		else:
			print("Не високосный")

# Task 59.
import datetime as dt

enter = input("Enter date: ")
date = dt.date(day=int(enter.split('.')[0]), month=int(enter.split('.')[1]), year=int(enter.split('.')[2]))
print(date + dt.timedelta(days=1))

# Task 60.
from math import floor

year = int(input("Enter year: "))
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_of_the_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7
print(days[day_of_the_week])

# Task 61.
import re

old = re.compile("[A-Z]{3}\d{3}")
new = re.compile('\d{4}[A-Z]{3}')
enter = input("Enter plate number: ")
if old.match(enter):
	print("Old plate number")
elif new.match(enter):
	print("New plate number")
else:
	print("Invalid plate number")

# Task 62.
import random

zero = [0, 00]
black = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
white = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
number = random.randint(0, 38)
if number == 0 or number == 38:
	print(f"Выпавший номер {number}")
elif number in white:
	print(f"""Выпавший номер: {number}...
	Выигравшая ставка: {number}
	Выигравшая ставка: белая
	Выигравшая ставка: четное""")
	if number < 19:
		print("\tВыигравшая ставка: от 1 до 18")
	else:
		print("\tВыигравшая ставка от 19 до 36")
elif number in black:
	print(f"""Выпавший номер: {number}...
	Выигравшая ставка: {number}
	Выигравшая ставка: черное
	Выигравшая ставка: нечетное""")
	if number < 19:
		print("\tВыигравшая ставка: от 1 до 18")
	else:
		print("\tВыигравшая ставка от 19 до 36")
