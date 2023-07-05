# Тема: Картежи, словари, множества
import random

# import random as r # - подключаем случайные числа
#
# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
#
# index = r.randint(0, len(colors) -1) # - что бы не печатался индекс 6, так как его нет (0-5)
#
# # for _ in range(10):     # _ -чтобы не задавать переменную,(больше нигде не используется, используется только в for)
# #     index = r.randint(0, len(colors) - 1)
# #     print(index)
#
# print((colors[index]))

# ДЗ от 0-10, угадай число. нужно вводить число и прога тебе говорит либо ты угадал с н попыток, либо ваше
# число больше/ меньше загаданного числа.

# import random as r
#
# lst = list('python') # преобразовывает строку в список
# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
#
# value = r.choice(colors)
# print(value)
# print(lst)

# создание уникального пароля
# import random as r
# r_string = 'qwertyuiopasdfghkjzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM123456789&'
# lst = list(r_string)
# r.shuffle(lst)  # метод shuffle ничего не возвращает, только тасует список (меняет индексы местами)
# # print(lst)
# # colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
# # value = r.choice(colors) - choice - метод рандома возвращаемый из списка
# temp = lst[:8]    # * - функции сообщаем о передаче списка
#
# if '&' in temp:
#     print(*temp, sep='')
# else:
#     temp.append('&')
#     print(*temp, sep='')
# # print(*lst[:8], sep='') # печатает 8 символов без пробела
# Картежи

#a = (1,1) # все что с запятой - это список неизменяемый <class 'tuple'>
# a = 3
# b = 4   #меняем значения  а и б создавая третью переменную можно записать подругому:
# temp = a
# a = b
# b = temp  либо
# a, b = 3, 4
# b, a = a, b
#
# print(a,b)

# l = ['пришла', 'весна'] # переворачиваем список
# l[1], l[0] = l[0], l[1]
# print(*l)

# def swap(a, b): # мы сами написали возрат картежа (меняет местами)
#     b, a = a, b
#     return a, b
# print(*swap(1,2))
# def swap(a):
#     x = a** 2
#     y = 2*a
#     z = a/a
#     return x,y,z
# temp = swap(2)
# print(temp)
# def swap1(a,b,c):
#     d = b*b -4*a*c
#     if d<0:
#     return print('нет корней')
#    if d == 0:
#     pass
#     return x1
#
# temp = swap(2)
# print(temp)

# t = 3, 3
# print(isinstance(t, tuple)) #встроенная функция

# a = 3, 4
# b = 4, 3
# print(a<b) # можно сравнивать картежи

# a = (1, 2) # картеж заменилии списком, поменяли местами и перевели обратно в картеж
# a=list(a)
# a[1], a[0] = a[0], a[1]
# a = tuple(a)
# print(a)

# x, y = input('введите х: '), input('введите у: ')
#
# print(x,y)

# {} - множество
# (1,)- картеж с одним значением
# () - список

# a=list()  # a=[]
# b =tuple() # b=(,) никак
# # c = set() # c = {} множество
#
# c= {'a','b','c', 'a'} # множество убивает повторяющиеся значения
# print(c)

# a = {1, 2, 3, 4}
# b = {2, 3, 5, 7, 11}
#
# # объединение
# print(a.union(b)) # {1, 2, 3, 4, 5, 7, 11}
# # пересечение
# print(a.intersection(b)) #  {2, 3}
# # разность
# print(a.difference(b)) # {1, 4}
# print(b.difference(a)) # {11, 5, 7}
# # симметричная разность
# print(a.symmetric_difference(b)) # {1, 4, 5, 7, 11}

# string ='телевидение'
# st = set(string)
# print(*st, sep='')

# lst = [2,3,5,7,11]
#
# for index, value in enumerate(lst):  # index, value - это название переменных, enumerate -возвращает картеж
#     print('индекс:', index, 'значение', value) #  название пемеренных не иммет значение - хоть i, v

# СЛОВАРЬ - обращаемся по ключевому слову, состоит из ключа и значения -> key: value
# d = {
#     'дмитриев': ['плотник', 'скульптор'],
#     'иванов': 'программист',
#     'петров': 'художник',
#     'сидоров': 'стоматолог',
#     1: None
# }
#
# d['петров'] = 'художник-оформитель'  # изменили значения ключа
# d['никитин'] = 'сисадмин' # добавили нового
# # print(d['иванов'])    # хотим узнат кто у нас иванов
# print(d['никитин'])
# for item in d:      # каждый item будет ключом
#     if isinstance(d[item], list):     # будем проверять картеж это лчто-то(лист) isinstance (true/false)
#         print(item + ':', d[item][1])   #меняя индекс 0 и 1 и в зависимости от желания
#     else:
#         print(item + ':', d[item])
# d = {
#     'дмитриев': 'скульптор',
#     'иванов': 'программист',
#     'петров': 'художник',
#     'сидоров': 'стоматолог'
# }
# d['никитин'] = 'сисадмин'
#
# # for item in d.values():     # выводим список всех значений
# #         print(item)
#
# for item in d.keys():     # выводим список всех ключей
#     print(item)

# d = {
#     'дмитриев': 'скульптор',
#     'иванов': 'программист',
#     'петров': 'художник',
#     'сидоров': 'стоматолог'
# }
# d['никитин'] = 'сисадмин'
#
#
# # for k, v in d.items():
# #
# #     # выводит всё ключ+значение ввиде картежа
# #     print(k, '->', v)
# if 'стоматолог' in d.values():      #поиск по словарю
#     print('он есть')

#   if 'а' in 'собака':
#     print('есть такая буква')       # проверяем есть ли "а" в слове 'собака'.

# СТРОКа- последовательность символов в какой-то кодировке.
# l = ['a', 'b', 'c']
# print('вот ABC первые 3 буквы:')
# for i, v in enumerate(l):
#     print('\t', i + 1, '->', v) # знак табуляции - \t

#есть 2 функции аним и антоним
# symbol = 'F'
# code = ord(symbol) # ord - порядковый номер из таблицы (кодов)
# print(code)

# code = 10000
# print(35, chr(code), 'C') # chr -функция вызова символа по коду

# code = 176
# print(35, '\u2710' + 'C')   #\u - вызов кодировки ascii unicode? \h,\y, \x -управляющая последовательность
#                             # если нам нужно напечатать \ - то вводим \\
#
#
# code = 176
# print(35, '\y' + 'C')

# string = 'Python Languages'
# num = '3Y'
# letter = 'FR3'
#
# let = '33.3'
#
# print(string.capitalize()) # предложение начинается со строчной. Python languages
# print(string.title())   # каждое слово начинается на заглавную Python Languages
# print(string.upper()) # все буквы большие PYTHON LANGUAGES
# print(string.lower()) # python languages
# print(num.isdigit())  # число ли
# print(letter.isupper())
# print(letter.isalpha())
# print(let.isnumeric())

# 2 метода
# string = 'Python Languages'
# # хотим разделить .split(' ') с пмощью разделителя пробел
# # lst = string.split(' ') # ['Python', 'Languages']
# lst = string.split('L') # ['Python ', 'anguages']
# print(lst)

# string = '                            Python Languages                                       '
# print(string)
# string = string.strip() # 'раздеть строку' - до первой и последней буквы убираем пробелы
# print(string)
# lst = string.split()
# print(lst)
#
# lst[0] = 'Java' # заменяем слово
# # метод соединить между собой с каким то разделителем
# new_string =' '.join(lst)
# print(new_string)
#
# # аптека улица фонарь
# blog_lst = ['Аптека','Улица',' Фонарь']
#
# new_blog_lst = ', '.join(blog_lst).capitalize()
#
# print(new_blog_lst) # Аптека, улица,  фонарь

string = 'аргентина манит негра'
new_str = ''.join(string.split())  # убираем все пробелы аргентинаманитнегра
print(new_str) # мне передали 0 аргументов