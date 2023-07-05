# import pickle
#
# f = open('dictinary.bin', 'rb')
# d = pickle.load(f)
#
#
# while True:
#     word = input('Введите слово для перевода (или QQ - для выхода): ')
#     if word == 'QQ':
#         break
#     if word in d:
#         print(f'Перевод слова: {word} -> {d[word]}')
#     else:
#         print('Я не знаю этого слова, но можете мне подсказать:')
#         new_word = input(f'Как переводится {word}: ')
#         d[word] = new_word
#
# with open('dictinary.bin', 'wb') as f:
#     pickle.dump(d, f)
# print('Спасибо, до свидания')
import math
import re

# d = {
#     'стол': 'table',
#     'стул': 'chair',
#     'яблоко': 'apple',
#     'автобус': 'bus',
#
# }
#
# keys = tuple(d.keys())
# values = tuple(d.values())
#
# with open('dictinary.txt', 'wt', encoding='utf-8') as f:
#     print(*keys, file=f)
#     print(*values, file=f)

# d = dict()
#
# with open('dictinary.txt', 'rt', encoding='utf-8') as f:
#     keys = f.readline().rstrip('\n')
#     values = f.readline().rstrip('\n')
#
# key_list = keys.split()
# value_list = values.split()
# lenght = len(key_list)
#
# for i in range(lenght):
#     d[key_list[i]] = value_list[i]
#
# print(d)

# Json - расширение для простоты

# Исключения - Exception

# name =input('kkk')
# print(nname) # NameError: - ошибка исключения и как ее избежать

# try:
#     print(nname)
# except NameError:
#     name = input('Ваше имя: ')
#     print('Вас зовут', name)
  # таким образом так как это имени нет он обходит эту ошибку

# вызываем несуществующий файл

     # f=open('text.txt') #  IndentationError: unexpected indent

# try:
#     f=open('text.txt')
# except IndentationError:
#     f = open('text.txt', 'w')
#     f.close()

# try:
#     f = open('text.txt')
#     #  какие-то действия с чтением файла #
#     f.close()
#     print('Все ок')
# except FileNotFoundError:
#     f = open('text.txt', 'w')
#     #  какие-то действия с записью файла #
#     f.close()
#     print('Файл был удален')
#     print('И он был создан')

# print('Считаем остаток от деления целого на 10!')
#
# value = int(input('от чего считаем остаток от деления (введите целое число): '))
# res = value % 10
# print(f'стоток от деления {value} на 10 будет {res}.')
# #  если ввести 5,1 - ValueError

# print('Считаем остаток от деления на 10!')
#
# try:
#     value = int(input('от чего считаем остаток от целого деления: '))
#     res = value % 10
#     print(f'стоток от деления {value} на 10 будет {res}.')
# except ValueError: # ошибка если ввели десятичное число 5,1 #
#     print('вас просили ввести целое число')

# print('Делим 10 на любое число!')
#
# try:
#     value = int(input('на что делим 10 (вежите целое чсло): '))
#     res = 10 / value
#     print(f'стоток от деления {value} на 10 будет {res}.')
# except ValueError: # ошибка если ввели десятичное число 5,1 #
#     print('вас просили ввести целое число')
# except ZeroDivisionError: # ошибка деления на ноль #
#     print('на ноль делить нельзя')
#
# print('Делим 10 на любое число!')
#
# try:
#     value = int(input('на что делим 10 (вежите целое чсло): '))
#     res = 10 / value
#     print(f'стоток от деления {value} на 10 будет {res}.')
# except Exception as exp: # ошибка если ввели десятичное число 5,1 #
#         print('вот что произошло ->', exp) # invalid literal for int() with base 10: '5/1'
#         print('вот что произошло ->', exp.__class__)  # <class 'ZeroDivisionError'> 0
# except ValueError: # ошибка если ввели десятичное число 5,1 #
#     print('вас просили ввести целое число')
# except ZeroDivisionError: # ошибка деления на ноль #
#     print('на ноль делить нельзя')

# print('Делим 10 на любое число!')
#
# try:
#     value = int(input('на что делим 10 (вежите целое чсло): '))
#     res = 10 / value
#     temp = value + 'привет'
#     print(f'стоток от деления {value} на 10 будет {res}.')
#
# except ValueError: # ошибка если ввели десятичное число 5,1 #
#     print('вас просили ввести целое число')
# except ZeroDivisionError: # ошибка деления на ноль #
#     print('на ноль делить нельзя')
# except Exception as exp: # ошибка если ввели десятичное число 5,1 #
#         print('вот что произошло ->', exp) # invalid literal for int() with base 10: '5/1'
#         print('вот что произошло ->', exp.__class__)  # <class 'ZeroDivisionError'> 0
# else:
#     print(f'стоток от деления {value} на 10 будет {res}.')

# print('Делим 10 на любое число!')
#
# try:
#     value = int(input('на что делим 10 (вежите целое чсло): '))
#     res = 10 / value
# except ValueError: # ошибка если ввели десятичное число 5,1 #
#     print('вас просили ввести целое число')
# except ZeroDivisionError: # ошибка деления на ноль #
#     print('на ноль делить нельзя')
# except Exception as exp: # ошибка если ввели десятичное число 5,1 #
#         print('вот что произошло ->', exp) # invalid literal for int() with base 10: '5/1'
#         print('вот что произошло ->', exp.__class__)  # <class 'ZeroDivisionError'> 0
# else: # если все в стандартном режиме
#     print(f'стоток от деления {value} на 10 будет {res}.')

# print('Делим 10 на любое число!')
# try:
#     value = int(input('на что делим 10 (вежите целое чсло): '))
#     res = 10 / value
#     print(f'стоток от деления {value} на 10 будет {res}.')
#
# # EOF - выдает ошибку если не закончен код End of File

# print('Делим 10 на любое число!')
# try:
#     value = int(input('на что делим 10 (вежите целое чсло): '))
#     res = 10 / value
# except ValueError: # ошибка если ввели десятичное число 5,1 #
#     print('вас просили ввести целое число')
# except ZeroDivisionError: # ошибка деления на ноль #
#     print('на ноль делить нельзя')
# except Exception as exp: # ошибка если ввели десятичное число 5,1 #
#         print('вот что произошло ->', exp) # invalid literal for int() with base 10: '5/1'
#         print('вот что произошло ->', exp.__class__)  # <class 'ZeroDivisionError'> 0
# else: # если все в стандартном режиме
#     print(f'стоток от деления {value} на 10 будет {res}.')
# finally:
#    print('Все относительно')  # выполняется в любом случае

# try:
#      f = open('informer.txt') # пробуем открыть несуществующий файл
#      print(f.read())
#      is_opened = True # устанавливаем флаг открытия
# except FileNotFoundError:
#     print('Файл не существует')
#     is_opened = False  # файл и не открывался, так как его и не было (флаг обнулился)
# finally:
#     if is_opened: # если файл был открыл успешно на чтение
#         print('Файл прочитан и закрыт')
#         f.close()
#     else:
#         print('файл и не открывался, так как его и не было')
#         # Файл не существует
#         # файл и не открывался, так как его и не было

# задача - организовать вечный цикл
# который будет продолжатся до тех пор пока не будет
# введено целое число
# первый вариант
# while True:
#     try:
#         value = int(input('Введите целое число: '))
#
#         print(f'число {value} .')
#         break
#     except ValueError: # ошибка если ввели десятичное число 5,1 #
#         print('вас просили ввести целое число')

# 2 вариант
# while True:
#     try:
#         value = int(input('Введите целое число: '))
#     except ValueError: # ошибка если ввели десятичное число 5,1 #
#         print('вас просили ввести целое число')
#     else:
#         print(f'число {value} .')
#         break
# 3 вариант
# while True:
#     try:
#         value = int(input('Введите целое число: '))
#     except ValueError: # ошибка если ввели десятичное число 5,1 #
#         print('вас просили ввести целое число')
#     else:
#         flag = True
#         print(f'число {value} .')
#         break
#     finally:
#         if flag:
#             print('До свидания')

# Throw Exception

# min_val = 1
# max_val = 10
# flag = False
# s_num = input(f'введите целое число от {min_val} до {max_val} ')
#
# try:
#     num = int(s_num)
#     if not min_val <= num <= max_val:
#         flag = True
#         raise ValueError('введеное число вне заданного диапазона')
# except ValueError as exp:
#     print('будьте внимательны:', exp)
# else:
#     if flag:
#         print(f'вас просили целое число, а вы ввели {s_num}')
#     print(f'число {num} введено верно')

#  assert - AssertionError - если утверждение не верно
# min_val = 1
# max_val = 10
# flag = False
#
# try:
#     text = input('введите текст: ')
#     assert len(text) >= 3 # утверждает что текст больше 3
# except AssertionError:
#     print('лина текста меньше 3х символов')
# МОдуль (бибдиотека) pickle  - опре
# PicklingError - проблема с сериализацией
# - проблема с десериализацией обьекта



# while True:
#     a = input('введите первое число ')
#     b = input('введите второе число ')
#     if a.isdigit() and b.isdigit():
#         if int(b) ==0:
#             print('на ноль делить нельзя')
#         else:
#             print(int(a)/int(b))
#             break
#     else:
#         print('необходимо вводить только числа.')

# while True:
#     a, b = input('введите первое число '),\
#         input('введите второе число ')
#         try:
#             print(int(a) / int(b))
#             break
#         except ZeroDivisionError:
#             print('на ноль делить нельзя')
#         except ValueError as exp:
#             print('необходимо вводить только числа')
#
# print('До свидания')



# Синтаксический сахар  - Syntax Suger - это любой имеющийся синтаксический элемент, механизм или способ,
# который дублирует другой --/--- но является более удобным или кратким либо выглядищим более успешно для человека

# def multy(*args):
#   print(f'мне передали {len(args)} аргументов')
# multy() # мне передали 0 аргументов
#
# multy(1, 2, 3) #  мне передали 3 аргументов
#
# def average(*args):
#  print(f'Среднее арифметическое списка: {sum(args)/len(args)}')
# average(1,2,3,4,5)

# print(print) # <built-in function print>

# output = print
# output('Hello') # поменяли командное словло print на output

# num_list = ['1', '2', '3', '4' ,'5']
# print(''.join(num_list)) # 12345
#
# num_list = [1, 2, 3, 4, 5]
# print(''.join(map(str, num_list))) # 12345
#
# num_list = [1, 2, 3, 4 , 5]
# str_list = list(map(str, num_list))
#
# print(str_list) # ['1', '2', '3', '4', '5']
#
# # map преобразует каждый элемент по заданному правилу - тут в строку str
#
# num_list = [1, 2, 3, 4 , 5]
# def double(x):
#  return x*2
# double_list = list(map(double, num_list))
# print(double_list) # [2, 4, 6, 8, 10] - увеличеваем в 2 раза


# lambda <аргументы>:<выражение с этими аргументами>
# num_list = [1, 2, 3, 4, 5]
# double = lambda x: x*2
# double_list = list(map(double, num_list))
# print(double_list) # [2, 4, 6, 8, 10] - увеличеваем в 2 раза
#
# double_list = list(map(lambda x: x**2, num_list))
# print(double_list) # [1, 4, 9, 16, 25]
#
# double_list = list(map(lambda x: math.sqrt(x), num_list))
# print(double_list) # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]


# import math
#
# num_list = [1, 2, 3, 4, 5]
# double_list = list(map(lambda x: math.pow(x, 3), num_list))
# print(double_list) # [1.0, 8.0, 27.0, 64.0, 125.0]

# string = ['банан', 'виноград', 'арбуз']
# s_list = sorted(string) # сортировка, по умолчанию по убыванию - а-я до 0-100
# print(s_list) # ['арбуз', 'банан', 'виноград']
#
# string = ['банан', 'виноград', 'арбуз']
# s_list = sorted(string, key=lambda x: x[3]) # сортировка, по умолчанию по убыванию - а-я до 0-100
# print(s_list)

# string = ['банан', 'виноград', 'арбуз']
# s_list = sorted(string, key=lambda x: x[2]) # сортировка, по умолчанию по убыванию - а-я до 0-100
# print(s_list) # ['арбуз', 'банан', 'виноград']
#
# string = ['банан', 'виноград', 'арбуз']
# s_list = sorted(string, key=len) # сортировка, по умолчанию по убыванию - а-я до 0-100
# print(s_list) # ['банан', 'арбуз', 'виноград']

# Regular Expressions
# средтво работы с текстом, позводяющий не только искать, но и редактировать исходный фрагмент по заданному образцу
# образец этот (pattern)

# s = 'телефон'
# s.find('еле')
# print(s)
import re

# pattern = '20' # мы будем искать 20 в строке
# test_str = '10 плюс 20 будет 30'
# res = re.search(pattern, test_str)
# print(res) # <re.Match object; span=(8, 10), match='20'>
# print(res.span()) # (8, 10) - показывает его индекс в строке
# test_str = '10 плюс 30 будет 40'
# res = re.search(pattern, test_str)
# print(res) # None

# import re
#
# pattern = r'\b\w{4}\b' # найдем все слова из 4х букв , \b\b - слово начинается и заканчивается \w{4} -  из 4х букв
# test_str = 'мама мыла раму, а папа был на пилораме'
# res = re.findall(pattern, test_str)
# print(res) # ['мама', 'мыла', 'раму', 'папа']
#
# pattern = r'\b\w{2}\b' # найдем все слова из 4х букв , \b\b - слово начинается и заканчивается \w{2} -  из 2х букв
# test_str = 'мама мыла раму, а папа был на пилораме'
# res = re.findall(pattern, test_str)
# print(res) # ['на']