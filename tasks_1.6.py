# Tasks 1.6

# Task 1.
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
print(f"In inch: {distance*12}")
print(f"In yards: {distance*0.33}")
print(f"In miles: {distance*0.00019}")

# Task 16.
r = int(input("Enter radius: "))
print(f"Square of ring: {math.pi*r**2}")
print(f"Voume of ball: {4/3*math.pi*r**3}")

# Task 17.
m = int(input("Enter mass of water: "))
delta_temp = int(input("Enter difference of temperature: "))
result = 4.186 * m * delta_temp
print(f"Кол-во энергии для достижения желаемого температурного изменения: {result}")
print(f"Стоимость 1 кВт/ч в центах{result * 2,78e-7 * 8.9}")

# Task 18.
r = int(input("Enter radius: "))
h = int(input("Enter hieght: "))
print(f"Volume of cylindr: {math.pi*r**2*h}")

# Task 19.
h = int(input("Enter hieght: "))
math.sqrt(0**2 + 2*9.8*h)

# Task 20.
p = int(input("Enter pressure: "))
v = int(input("Enter volume: "))
t = int(input("Enter temperature: "))
print((p*v)/(8.314*(t+273.15)))  # 98471.67

# Task 21. To be continue...
