# Файл утерян на рабочем Lenovo, задания 85-104 были выполнены

# # Task 104.
# dict_numbers = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#
#
# def hex2int(s: str):
#     if s.isdigit():
#         print(s)
#     else:
#         for key, val in dict_numbers.items():
#             if s == val:
#                 print(key)
#
#
# def int2hex(i: int):
#     if 0 <= i <= 15:
#         if i in dict_numbers.keys():
#             print(dict_numbers.get(i))
#     else:
#         print('Invalid int')
#
# hex2int("C")
# int2hex(10)

# Task 105. Skip (утеряны данные с прошлых упражнений)

# # Task 106.
# def isyear(year):
#     if year % 400 == 0:
#         return True
#     else:
#         if year % 100 == 0:
#             return False
#         else:
#             if year % 4 == 0:
#                 return True
#             else:
#                 return False
#
#
# month_dict = {31: [1, 3, 5, 7, 9, 11], 30: [4, 6, 8, 10, 12], 27: 0, 28: 0}
#
#
# def how_much_days(month: int, year: int):
#     if isyear(year):
#         month_dict[27] = 2
#     else:
#         month_dict[28] = 2
#     for key, val in month_dict.items():
#         if month in val:
#             return key


# how_much_days(11, 1980)

# # Task 107.
# def fraction(x: int, y: int):
#     for n in range(y, 2, -1):
#         if x % n == 0 and y % n == 0:
#             x /= n
#             y /= n
#     return int(x), int(y)
#
#
# print(fraction(6, 63))

# # Task 108.
# def cook(num: int, item: str):
#     lst = ['1 cup == 16 tablespoons', '1 tablespoons == 3 teaspoons']
#     if item == 'cup':
#         print(num, item)
#     elif item == 'tablespoons' and num % 16 > 0:
#         cups = num // 16
#         tablespoons = num % 16
#         print(f'{cups} cups, {tablespoons} tablespoons')
#     elif item == 'teaspoons' and num % 3 > 0:
#         cups = num // 48
#         tablespoons = (num % 48) // 3
#         teaspoons = (num % 48) % 3
#         print(f'{cups} cups, {tablespoons} tablespoons, {teaspoons} teaspoons')
#
#
# cook(59, 'teaspoons')

# # Task 109.
# def magic_date(day, month, year):
#     if day * month == int(str(year)[2:]):
#         return True
#     else:
#         return False
#
#
# print(magic_date(10, 6, 1960))
# print(magic_date(11, 6, 1960))
