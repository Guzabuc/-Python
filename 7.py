# # Цикл с continue
#
# counter = 0
# while True:
#     counter+= 1
#     if counter>10:
#         break
#     if counter % 2: # пропустить какое-то действие и начинается следующая итерация
#         continue
#     print(counter)
#
# print('Цикл прерван')

# Файловая система

# import os
#
# print(os.getcwd())

# import os
#
# root = os.getcwd()
#
# os.mkdir('images') # создание папки в проекте

# import os # КОРНЕВАЯ СИСТЕМА ПРОЕКТА
#
# root = os.getcwd() # путь нашего проекта
# print('Мы пока здесь:', root)
# if not os.path.isdir('images'): # - дикертория
#     os.mkdir('images') # создание папки в проекте под названием 'images'
# os.chdir('images')  # меняем каталог(путь к файлам) на images
#
# print('А теперь здесь:', os.getcwd())
# os.chdir(root)
# os.chdir('..')  # вверх на один уровень (если забыл где находишься)
# print('Мы пока здесь:', root)

# import os
#
# root = os.getcwd()
# if not os.path.isdir('images'): # - дикертория
#     os.mkdir('images')
#
# files = os.listdir(root) # пока жи мне какие есть файлы в корнивике
# print(files) # ['.idea', '2.py', '3.py', '4.py', '5.py', '6.py', '7.py', 'Cesar.py', 'cropped.JPEG', 'grayscale.JPEG',
# # 'h_flipped.JPEG', 'image.png', 'image1.png', итд показывает все файлы и папки в корневике
#
# images = [] # пока пустой список для файлов изображения
#
# for file in files:
#     if os.path.isfile(file) and \
#             (file.endswith('.png')
#              or file.endswith('.JPEG')):  # and file.endswith('.JPEG')
#         images.append(file)
# # print(images)  - проверяем чтобы файлы были тетперь в images
# # \ - 'это знак переноса, чтобы не писать в одну длинную строку
# for image in images:
#     os.replace(image,'images/' + image) # перенесли все файлы в папку images

# for image in images:
#     os.remove(image) # из списка удаляются все файлы
#     os.rename(image1, image1) # переименовать
#     os.walk() - рекрусивный обход всех папок

# import os
# import sys
#
# root = os.getcwd()

# file = open('info.txt', 'r') # открываем файл , 'r' - файл открывается по умолчанию для чтения
# или
# file = open('info.txt', 'w') # открываем файл , 'w' - файл открывается для записи
# или


#   в любом файле есть указатель,  at  - передвигает курсор к последнему символу в файле

# if os.path.isfile('info.txt'):
#     file = open('info.txt', 'rt', encoding='utf-8')  # файл открывается для записи и он будет текстовый
#     print('Имя файла:', file.name)
#     print('Режим:', file.mode)
#     print('Кодировка:', file.encoding)
#
# # file.write(root) # записывает в файл его путь
#
#     file.read(3)    # количество символов в файле
#     temp = file.read(5)
#
#     file.close()
#     print(temp)
# else:
#     print('Файл не существует!')


# if os.path.isfile('info.txt'):
#     file = open('info.txt', 'rt', encoding='utf-8')  # файл открывается для записи и он будет текстовый
#     print('Имя файла:', file.name)
#     print('Режим:', file.mode)
#     print('Кодировка:', file.encoding)
#
# # file.write(root) # записывает в файл его путь
#
#     file.read(3)    # количество символов в файле пропускает курсор тут 3
#     user = file.read(5)  # считывает это количество символов тут 5
#     file.read(1) # снова пропускает тут 1
#     student = file.read(7) # считывает это количество символов тут 7
#
#     file.close()
#     print(f'А {user} - {student}!!!') # ответ : А Users - Student!!!
# else:
#     print('Файл не существует!')

# fname = 'info.txt'

# if os.path.isfile('info.txt'):
#     file = open('info.txt', 'rt', encoding='utf-8')  # файл открывается для записи и он будет текстовый
#     print('Имя файла:', file.name)
#     print('Режим:', file.mode)
#     print('Кодировка:', file.encoding)
#
#     string = file.read() #  123
#     lst = list(string)
#     summ = 0
#
#     file.close()
#     for i in lst:
#         if i.isdigit():
#             summ += int(i)
#
#     print(summ)
# else:
#     print('Файл не существует!')



# if os.path.isfile('info.txt'):
#     file = open('fname.txt', 'wt', encoding='utf-8')  # файл открывается для записи и он будет текстовый
#     print('Имя файла:', file.name, file=sys.stdout)
#     print('Режим:', file.mode, file=file)
#     print('Кодировка:', file.encoding, file=file)
# тут print напечатал внутрь файла.

# import os
#
# root = os.getcwd()
# fname = 'info.txt'
# str = ''
# if os.path.isfile(fname):
#     file = open(fname, 'rt', encoding='utf-8')
#     s = file.readline()
#
#     while s != '':
#         str += s
#         s = file.readline()
#
#     file.close()
#
#     print(str)

# import os
#
# root = os.getcwd()
# fname = 'info.txt'
#
# if os.path.isfile(fname):
#     file = open(fname, 'rt', encoding='utf-8')
#     s = file.read()
#
#     file.close()
#
#     res = s.splitlines()
#     print(res)

# import os
#
# root = os.getcwd()
# fname = 'info.txt'
#
# if os.path.isfile(fname):
#     with open(fname, 'rt', encoding='utf-8') as file: # более лучшая версия
#         s = file.read()
#
#     res = s.splitlines()
#     print(res)

# import os
#
# root = os.getcwd()
# fname = 'info.txt'
# d = []
#
# list_1 = [1, 3, 5, 8, 12, 24, 37, 55, 89]
# list_2 = [2, 4, 5, 8, 14, 24, 39, 58, 89]
#
# set1 = set(list_1)
# set2 = set(list_2)
#
# temp = list(set1.intersection(set2))
#
# if os.path.isfile(fname):
#     with open(fname, 'wt', encoding='utf-8') as file: # более лучшая версия
#         print(*temp, sep=', ', file=file) # 8, 24, 5, 89

# import os
#
# root = os.getcwd()
# fname = 'info.txt'
#
#
# list_1 = [1, 3, 5, 8, 12, 24, 37, 55, 89]
# list_2 = [2, 4, 5, 8, 14, 24, 39, 58, 89]
# temp = []
#
# for item in list_1:
#     if item in list_2:
#         temp.append(item)
#
#
# if os.path.isfile(fname):
#     with open(fname, 'wt', encoding='utf-8') as file: # более лучшая версия
#         print(*temp, sep=', ', file=file)  #   8, 24, 5, 89

# import pickle  # pickling - консервация данных (серилиализация) сохраняем всю инфу в виде последовательности битов
#
# d = {
#     'стол': 'table',
#     'стул': 'chair'
# }
#
# fname = 'dictinary.bin'
#
# with open(fname, 'wb') as file:
#     pickle.dump(d, file)

import pickle  # pickling - консервация данных

fname = 'dictinary.bin'

with open(fname, 'rb') as file:
    d = pickle.load(file)

print(d) #  {'стол': 'table', 'стул': 'chair'}


#  {'стол': 'table', 'стул': 'chair'} - перевод словаря
# вводим table - показывает перевод
# тоже самое со столом
# вводим яблоко - такого слова нет - введите перевод
# он добавиться и в словаре теперь три слова

import pickle  # pickling - консервация данных (серилиализация) сохраняем всю инфу в виде последовательности битов

d = {
    'стол': 'table',
    'стул': 'chair'
    }

word = input('')

if word in d:
    print()
else:
    print()
    print()
    new_word = input()
    d[word] = new_word