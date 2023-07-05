# source = 'город рим' # нужно получить - миргород - дорог город миргород
#
# lst = source.split()
#
# print(lst[0][::-1], lst[0], lst[1][::-1]+lst[0])

# нужно посчитать сколько буква встречается в предложении - город рим (г-1, ,о-2)
# source = 'город рим'
# d = dict()
#
# source = ''.join(source.split()) # убрали пробелы
# # первый способ
# # for letter in source:
# #     if letter in d:
# #         d[letter] += 1
# #     else:
# #         d[letter] = 1
#
# # второй способ
# for letter in source:
#     if letter not in d:
#         d[letter] = 1
#     else:
#         d[letter] += 1
#
# for k, v in d.items():
#     print(k, v, sep='-')


# тернарный оператор

# t = 20 #(если t > 20, тепло, иначе прохладно)
#
# print('тепло') if t >= 20 else print('прохладно')

# [если ИСТИНА ] [условие] [иначе] [ЛОЖЬ]

# ПОИСК в строке

# string = 'видеть, вертеть, смотреть'
#
# # find(что искать, старт, стоп)
# index = string.find('еть')
# print(index) # 3 - начиная с нуля
# index = string.find('еть', 10)
# print(index) # 12 - начиная с 0 или с начало строки 10
# index = string.find('еть', 15, 20)
# print(index)   # -1 - ничего не нашел в этом промежутке

# phone = '+7-012-345-67-89'
# print('Исходная строка', phone)
#
# spaced_phone = phone.replace('-',' ')  # .replace - замена символов в строке
#
# print('Телефон через пробел', spaced_phone)
#
# temp = phone.replace('-','(', 1) # replace('-','(', 1) - замена символов один(1) раз
# print(temp)
# temp_2 = temp.replace('-',')', 1)
# print(temp_2)

# string = 'тиливизор'
# print(string.replace('и','е', 2))

# lst = [5, 1, 3, 2, 4]
# lst.sort() # [1, 2, 3, 4, 5] о умолчанию False сортировка по возрастанию - это метод
# lst.sort(reverse=True) # [5, 4, 3, 2, 1]
#
# print(lst)
# print(sorted(lst)) # [1, 2, 3, 4, 5] ее можно писать в print, возвращает функцию
# print(sorted(lst, reverse=True)) # [5, 4, 3, 2, 1]

# ФОРМАТИРОВАНИЕ СТРОКИ

# placeholder
# %5d - число '     45'
# %s - строка
# %f - float

# name = 'Виктор'
# age = 19
# height = 114.51
# # %15s - где 15 это количество пробелов отведенные под этот параметр
# f_string ='%15s, \nвозраст: %2d лет, \nрост: %6.1f см' %(name, age,height)
# print(f_string)

# введите целое число
# min_val = 5
# max_val = 50
#
# nm_str = 'введите целое число от %d до %d' % (min_val, max_val)
# print(nm_str )

# именованный
# name = 'Виктор'
# age = 19
# height = 114.51
#
# f_str = 'Имя : {N}, возраст: {A} лет, рост {H}'.format(N=name, A=age,H=height)
#
# print(f_str)

# name = 'Виктор'
# age = 19
# height = 114.51
#
# f_str = f'Имя : {name}, возраст: {age} лет, рост: {height:.1f}'
#
# print(f_str)


# Списочные выражения
# a =[]
# for i in range(1, 11):
#     a.append(i)
# print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  - по простому

# a = [i for i in range(1, 11)]
# print(a) #  заняло 2 строчки

# a = [i for i in range(1, 101) if i % 10 == 5]
# print(a) # [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

# ip = '198.162.100.101'
# a = [int(i) for i in ip.split('.')]
# print(sum(a)) # 561
#
# a = ip.split('.')
# summ = 0
# for i in a:
#     summ += int(i)
#
# print(summ) # 561

# a = '5 6 7 9'

# первый вариант
# s = ''.join(a.split())
# summ =0
# for x in s:
#     summ += int(x)
# print(summ) # 27

# n = sum([int(x) for x in a.split()])
# print(n) # 27

# МОДУЛИ
# первый вариант
# import lib # обращается к файлу lib
#
# lib.say_hello('Tom')
# lib.div(2,3)
# # 2 вариант
# from lib import div, say_hello # обращается к файлу lib конкретно к div, say_hello
#
# say_hello('Tom')
# div(2,3)
# # 3 вариант
# from lib import * # обращается к файлу lib обрщается ко всем функциям
#
# say_hello('Tom')
# div(2,3)
#
# print(__name__)

# менеджеры пакета / библиотеки

from PIL import Image # создание изображения
# первый вариант
# new_image = Image.new("RGB", (100,100), (0,0,0))
#
# new_image.save('image.png', 'PNG')
# new_image.show()
# 2й вариант

from PIL import ImageDraw

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

W, H = (100, 100)
canvas = Image.new("RGB", (W, H), BLACK)  # создали холcт
draw = ImageDraw.Draw(canvas)  # коробка с инструментами

draw.line((0, 0, W, H), fill=YELLOW, width=2)
draw.line((100, 0, 0, 100), fill=YELLOW, width=2)
draw.line((50, 0, 50, 100), fill=YELLOW, width=2)
draw.line((0, 50, 100, 50), fill=YELLOW, width=2)
canvas.save('image.png', 'PNG')
canvas.show()
