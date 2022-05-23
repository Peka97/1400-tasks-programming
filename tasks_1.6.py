# Tasks 1.6

# Task 1.
import time

name = "Ivan"
email = "vk-vk.karasev@yandex.ru"
print(name + " " + email)

# Task 2.
name = input("Enter your name: ")
print("Hello, " + name)

# Task 3.
lenght = input("Enter lenght of your room: ")
width = input("Enter width of your room: ")
print("Square of your room: ", float(lenght * width))

# Task 4.
lenght = input("Enter lenght of your garden: ")
width = input("Enter width of your garden: ")
print("Square of your garden in acrs: ", lenght * width / 43560)

# Task 5.
bottle_lt1 = input("Enter count of bottle with volume less than 1 liter: ")
bottle_gt1 = input("Enter count of bottle with volume more than 1 liter: ")
print("My cash: " + bottle_lt1 * 0.10 + bottle_gt1 * 0.25)

# Task 6.
price = input("Enter price of your order: ")
print("Tax: " + price * 0.20 + "\nTips: " + price * 0.18)

# Task 7.
num = input("Enter count: ")
result = 0
print(f"Sum of all positive nums from 1 to {num} is {(num * (num + 1)) / 2}")

# Task 8.
souvenir = input("Enter count of souvenirs: ")
bauble = input("Enter count of baubles: ")
print(f"Total weight: {souvenir * 75 + bauble * 112}g")

# Task 9.
first_deposit = int(input("Enter your first deposit: "))
print("1 year: %.2f; 2 year: %.2f; 3 year: %.2f" % (first_deposit * 1.04, first_deposit * 1.04 ** 2,
                                                    first_deposit * 1.04 ** 3))

# Task 10.
import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(math.log10(a))
print(a ** b)

# Task 11.
USA_value = float(input("Enter MPG: "))
Canada_value = 235.22 / USA_value
print(Canada_value)

# Task 12.
import math as m

point_1 = input("Enter first point across space: ")
point_2 = input("Enter second point arcoss space: ")
t1 = m.radians(int(point_1.split()[0]))
g1 = m.radians(int(point_1.split()[1]))
t2 = m.radians(int(point_2.split()[0]))
g2 = m.radians(int(point_2.split()[1]))
print(6371.01 * m.acos(m.sin(t1) * m.sin(t2) + m.cos(t1) * m.cos(t2) * m.cos(g1 - g2)))

# Task 13.
change = int(input("Enter change: "))
cents_25 = change // 25
cents_10 = change % 25 // 10
cents_5 = change % 25 % 10 // 5
cents_1 = change % 25 % 10 % 5
print(cents_25, cents_10, cents_5, cents_1)

# Task 14.
import math

heigth_in_foot = int(input("Enter your height in foot: "))
height_in_inch = int(input("Enter your height in inch: "))
print("Your height in cm: ", heigth_in_foot * 12 * 2.54, " and ", height_in_inch * 2.54)

# Task 15.
distance = int(input("Enter distance: "))
print(f"In inch: {distance * 12}")
print(f"In yards: {distance * 0.33}")
print(f"In miles: {distance * 0.00019}")

# Task 16.
r = int(input("Enter radius: "))
print(f"Square of ring: {math.pi * r ** 2}")
print(f"Voume of ball: {4 / 3 * math.pi * r ** 3}")

# Task 17.
m = int(input("Enter mass of water: "))
delta_temp = int(input("Enter difference of temperature: "))
result = 4.186 * m * delta_temp
print(f"Кол-во энергии для достижения желаемого температурного изменения: {result}")
print(f"Стоимость 1 кВт/ч в центах{result * 2, 78e-7 * 8.9}")

# Task 18.
r = int(input("Enter radius: "))
h = int(input("Enter hieght: "))
print(f"Volume of cylindr: {math.pi * r ** 2 * h}")

# Task 19.
h = int(input("Enter hieght: "))
math.sqrt(0 ** 2 + 2 * 9.8 * h)

# Task 20.
p = int(input("Enter pressure: "))
v = int(input("Enter volume: "))
t = int(input("Enter temperature: "))
print((p * v) / (8.314 * (t + 273.15)))  # 98471.67

# Task 21.
b = int(input("Enter Triangle base length: "))
h = int(input("Enter Triangle height: "))
print(f"Triangle square: {(b * h) / 2}")

# Task 22.
s1 = int(input("Enter s1: "))
s2 = int(input("Enter s2: "))
s3 = int(input("Enter s3: "))
s = (s1 + s2 + s3) / 2
print(f"Triangle square: {math.sqrt(s * (s - s1) * (s - s2) * (s - s3))}")

# Task 23.
s = int(input("Enter s: "))
n = int(input("Enter n: "))
print(f"Right triangle square: {(n * s ** 2) / 4 * math.tan(math.pi / n)}")

# Task 24.
days = int(input("Enter count of days: "))
hours = int(input("Enter count of hours"))
minutes = int(input("Enter count of minutes: "))
seconds = int(input("Enter count of seconds: "))
print(f"Total seconds: {days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds}")

# Task 25.
seconds = int(input("Enter count of seconds: "))
D = seconds // 86400
H = (seconds % 86400) // 3600
M = (seconds % 3600) // 60
S = seconds % 60
print('Total time: %.02i:%.02i:%.02i:%.02i' % (D, H, M, S))

# Task 26.
import time

print(time.asctime())

# Task. 27.
import datetime as dt
import math

now = dt.datetime.now()
year = int(dt.datetime.strftime(now, '%Y'))
a = year % 19
b = math.floor(year / 100)
c = year % 100
d = math.floor(b / 4)
e = b % 4
f = math.floor((b + 8) / 25)
g = math.floor((b - f + 1) / 3)
h = (19 * a + b - d - g + 15) % 30
i = math.floor(c / 4)
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = math.floor((a + 11 * h + 22 * l) / 451)
mount = math.floor((h + l + 7 * m + 114) / 31)
day = 1 + ((h + l - 7 * m + 114) % 31)
print("Date of Easter: ", year, mount, day)

# Task 28.
weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))
BMI = weight/height**2

# Task 29.
import math

T = int(input("Enter temperature of air: "))  # Less then 10C
V = int(input("Enter speed of wind: ")) # More then 4.8 km\h
WCI = math.ceil(13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16)
print(f"Temperature with considering wind: {WCI}")

# Task 30.
C = float(input("Enter Cels: "))
K = C * 274.15
F = C * 33.8
print(f"Kelvins: {K}\nFarengeight: {F}")

# Task 31.
kPa = float(input("Enter count of kPa: "))
PSI = kPa * 0.145038
MOM = kPa * 7.5
A = kPa * 0.009869
print(PSI, MOM, A)

# Task 32.
num = input("Enter num: ")
result = 0
for i in num:
    result += int(i)
print(result)

# Task 33.
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))
lst = [num1, num2, num3]
num_max = max(lst)
num_min = min(lst)
lst.remove(num_min)
lst.remove(num_max)
num_med = lst[0]
print(num_min, num_med, num_max)

# Task 34.
count = int(input("Enter count of breads: "))
price = 3.49
sale = 0.6
print(f"Bread price: {price}")
print(f"Bread sale price: {price*sale}")
print(f"Total price: {price*sale*count}")
