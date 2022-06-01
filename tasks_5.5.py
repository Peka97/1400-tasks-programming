# Tasks 5.5

# # Task 110.
# result = []
# while True:
#     el = int(input("Enter num: "))
#     if el == 0:
#         break
#     result.append(el)
# print(result)

# # Task 111.
# temp = []
# while True:
#     el = int(input("Enter num: "))
#     if el == 0:
#         break
#     temp.append(el)
# print(temp)
# result = []
# while len(temp) != 0:
#     max_num = max(temp)
#     print(max_num)
#     for idx, el in enumerate(temp):
#         if el == max_num:
#             result.append(el)
#             temp.remove(el)
#             break
# print(result)

# # Task 112.
# from copy import copy
#
# lst = []
# while True:
#     num = int(input("Enter nums (5 or more): "))
#     if num == 0:
#         break
#     lst.append(num)
#
#
# def func(n):
#     copy_lst = copy(lst)
#     for _ in range(n):
#         copy_lst.remove(max(copy_lst))
#         copy_lst.remove(min(copy_lst))
#     return copy_lst
#
#
# print(func(2))

# # Task 113.
# lst = []
# while True:
#     word = input("Enter word: ")
#     if word == '0':
#         break
#     lst.append(word)
# lst = set(lst)
# print(lst)

# # Task 114.
# lst = []
# while True:
#     num = int(input("Enter num: "))
#     if num == 999:
#         break
#     lst.append(num)
#
#
# def func(l):
#     result = []
#     for el in l:
#         result.append(el) if el < 0 else None
#     for el in l:
#         result.append(el) if el == 0 else None
#     for el in l:
#         result.append(el) if el > 0 else None
#     return result
#
#
# print(func(lst))

# # Task 115.
# def func(num):
#     result = []
#     for x in range(1, num):
#         if num % x == 0:
#             result.append(x)
#     return result
#
#
# print(func(50))

# # Task 116.
# def func(num):
#     result = []
#     for x in range(1, num):
#         if num % x == 0:
#             result.append(x)
#     print(result)
#     return True if sum(result) == num else False
#
#
# print(func(50))
# print(func(28))

# # Task 117.
# text = "Contractions include: don’t, isn’t, and wouldn’t."
#
#
# def format(t):
#     lst = [',', ':', '.']
#     for el in lst:
#         t = t.replace(el, '')
#     return t
#
#
# def func(txt: str):
#     txt = format(txt)
#     return txt.split()
#
#
# print(func(text))

# # Task 118.
# text = input("Enter text: ")
#
#
# def format(t):
#     lst = [',', ':', '.', '?']
#     for el in lst:
#         t = t.replace(el, '')
#     t = t.lower()
#     return t
#
#
# def func(txt: str):
#     txt = format(txt)
#     return txt.split()
#
#
# txt = func(text)
# print(txt)
# x = 0
# y = -1
# pallindrome = True
# if len(txt) % 2 == 0:
#     for _ in range(int(len(txt) / 2)):
#         if txt[x] == txt[y]:
#             x += 1
#             y -= 1
#         else:
#             pallindrome = False
#             break
# else:
#     for _ in range(int((len(txt) / 2) - 1)):
#         if txt[x] == txt[y]:
#             x += 1
#             y -= 1
#         else:
#             pallindrome = False
#             break
# print(f"Text is pallindrome") if pallindrome is True else print(f"Text is not pallindrome")

# # Task 119.
# from statistics import mean
#
# lst = []
# while True:
#     num = input("Enter num(or SPACE for QUIT): ")
#     if num == " ":
#         break
#     lst.append(int(num))
#
#
# def func(l):
#     result = []
#     result_2 = []
#     result.append(mean(l))
#     for el in l:
#         if el < result[0]:
#             result_2.append(el)
#     return result, result_2
#
#
# print(func(lst))

# # Task 120.
# lst = ['яблоки', "апельсины", "бананы", "лимоны"]
#
#
# def func(l):
#     reply = ""
#     for el in lst[0:-1]:
#         reply += f"{el}, "
#     reply += f'и {lst[-1]}'
#     return reply
#
# print(func(lst))

# # Task 121.
# from random import randint
#
#
# tiket = [1, 4, 6, 9, 10, 14]
#
#
# def func(t):
#     rand = set()
#     x = 0
#     while len(rand) < 7:
#         rand.add(randint(1, 49))
#     for el in t:
#         if el in rand:
#             x += 1
#     return True if x == 6 else False


# print(func(tiket))

# # Task 122.
# words = ['computer', 'Computer', 'office', 'Office', 'Office!']
#
#
# def pig_latina(word: str):
#     glas = ['a', 'e', 'u', 'i', 'o']
#     signs = ['!', '?']
#     s = ''
#     for sign in signs:
#         if sign in word:
#             s += sign
#             word = word.replace(sign, '')
#     if word[0].lower() in glas:
#         if word[0] == word[0].capitalize():
#             return word.capitalize() + "way" + s
#         return word + 'way' + s
#     else:
#         lst = []
#         for letter in glas:
#             if letter in word.lower():
#                 lst.append(word.index(letter))
#         idx = min(lst)
#         if word[0] == word[0].capitalize():
#             return word[idx].upper() + word[idx + 1:] + word[:idx].lower() + f'ay' + s
#         return word[idx:] + word[:idx] + f'ay' + s
#
#
# print(pig_latina(words[0]))
# print(pig_latina(words[1]))
# print(pig_latina(words[2]))
# print(pig_latina(words[3]))
# print(pig_latina(words[4]))


# Task 124. Skip

# # Task 125.
# def createDeck():
#     suits = ['s', 'c', 'd', 'h']
#     nominals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
#     cards = []
#     for suit in suits:
#         for nominal in nominals:
#             cards.append(f'{nominal}{suit}')
#     return cards
#
#
# def shuffle(deck):
#     from random import randint
#     result = []
#     x = len(deck)
#     while x != 0:
#         result.append(deck.pop(randint(0, x - 1)))
#         x -= 1
#     return result
#
#
# # Task 126.
# def deal(players: int, count: int, deck: list):
#     from random import randint
#     print(deck)
#     print(len(deck))
#     result = []
#     for x in range(players):
#         result.append([])
#         for __ in range(count):
#             result[x].append(deck.pop(randint(0, len(deck)-1)))
#     return result
#
#
# print(deal(4, 5, shuffle(createDeck())))

# # Task 127.
# lst = [1, 2, 3, 4, 5]
# lst_2 = [2, 3, 4, 5, 1]
#
#
# def sorted(l):
#     for x in range(len(l)-1):
#         if l[x] > l[x+1]:
#             return False
#     return True
#
#
# print(sorted(lst))
# print(sorted(lst_2))

# # Task 128.
# def countRange(l: list, min: int, max: int):
#     result = 0
#     for el in l:
#         if min < el < max:
#             result += 1
#     return result
#
#
# print(countRange([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 5, 6, 5, 4], 3, 6))

# Task 129. Skip

# # Task 130.
# def isunary(array: str):
#     x = 0
#     for el in array:
#         if el.isdigit():
#             x += 1
#     return True if x > 1 else False
#
#
# print(isunary('1 + 2'))
# print(isunary('-1'))

# Task 131, 132. Skip. Lexems from 129.

# # Task 133.
# def isSublist(larger: list, smaller: list):
#     start = 1
#     for x in range(len(larger)):
#         if start < len((larger)):
#             if smaller == [larger[start], larger[start + len(smaller) - 2]]:
#                 return True
#         else:
#             if smaller == [larger[-2], larger[-1]]:
#                 return True
#         start += x
#     return False
#
#
# print(isSublist([1, 2, 3, 4], [3, 4]))

# # Task 134.
# def genSublist(l):
#     result = []
#     for el in l:
#         result.append(el)
#     start = 0
#     for x in range(1, len(l)):
#         if start < x:
#             result.append(l[start:x + 1])
#             start += 1
#     result.append(l)
#     return result
#
#
# print(genSublist([1, 2, 3]))
# print()
# print(genSublist([1, 2, 3, 4]))  # Не выводит подмножества длинной больше 2х(кроме самого множества)

# # Task 135.
# def eratosphen(limit):
#     array = []
#     for el in range(0, limit + 1):
#         array.append(el)
#     array[1] = 0
#     p = 2
#     for_delete = []
#     while p < limit:
#         for i in range(p * 2, limit + 1, p):
#             array[i] = 0
#         p += 1
#         while p < limit and array[p] == 0:
#             p += 1
#     for _ in range(array.count(0)):
#         array.remove(0)
#     return array
#
#
# print(eratosphen(10))
