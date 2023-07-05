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

# import math
#
# lst = [1, 2, 3, 4, 5]
# power = lambda x, y: math.pow(x, y)
# # .pow возведение в степень
# res = list(map(lambda x: power(x, 2), lst))
# print(*res) # 1.0 4.0 9.0 16.0 25.0

# rus = ['стул', 'стол', 'яблоко']
# eng = ['chair', 'table', 'apple']
# #  - zip( - с его помощью можно соединить два списка и на выходе возвращает картеж, в нашем случае словарь
# d = dict(zip(rus,eng))
# print(d) # {'стул': 'chair', 'стол': 'table', 'яблоко': 'apple'}

# проверяем правильность написания URL(адрес http/ https... и название почты

# import re
# # найдем все слова в сырой строке r из 4х букв , \b\b - слово начинается и заканчивается \w{4} -  из 4х букв
# # есть ли в стороке цифры \d от 0 до 9
# # pattern = r'\d'
# # есть ли в стороке цифры \d от 0 до 9 и трехзначное {3} (112)
# pattern = r'\d{3}'
# test_str = 'Для экстренных вызовов 11'
# # больше одного значения re.findall (мама мыла раму...)
# #  result = re.findall(pattern, test_str)
# # одно значениe re.search (мама мыла раму...)
# result = re.search(pattern, test_str)
#
# print('Цифры есть') if result else print('Цифры есть') # Цифры есть
#
# if result: # если в строке только 11, то он выдает TypeError: 'NoneType' object is not subscriptable
#     print(result[0], result.span()) #  с этим выражение ошибку не выдает 112 (23, 26)

# import re
#
# pattern = r'начало!\Z' #  заканчивается ли строка на ( начало! ) \Z - конец строки
# test_string = 'Главное - начало!'
# result = re.search(pattern, test_string)
#
# if result:
#     print(result[0], result.span()) # начало! (10, 17)
# else:
#     print('Нету')

# import re
#
# pattern = '[0-5][0-9]' #  от 00 до 59 - результат 07 (8, 10)
# test_string = 'Время - 07:45!'
# result = re.search(pattern, test_string) # тут оператор ище один раз
# if result:
#     print(result[0], result.span()) # начало! (10, 17)
# else:
#     print('Нету')

# import re
#
# pattern = '[0-5][0-9]' #  от 00 до 59 - результат ['07', '45']
# test_string = 'Время - 07:45!'
# result = re.findall(pattern, test_string)  # находит все значения
# print(result)

# import re
#
# pattern = '[^абвгд]' #  отобразить всё кроме всег, что в скобке
# test_string = 'АБВГДейка - детская передача!'
#
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
#
# # print(result) Если оставить простой print(result), то у нас будет нечитаемый
# # ответ (список)['е', 'й', 'к', ' ', '-', ' ', 'е', 'т', 'с', 'к', 'я', ' ', 'п', 'е', 'р', 'е', 'ч', '!']
#
# # print(* - превращает в строку
# print(*result, sep='') # ейк - етскя переч!

# import re
#
# pattern = r'\((.+?)\)' #  находим все что находится в скобках
# test_string = 'Поиск по образцу (pattern)!'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
#
# print(*result, sep='') # pattern

# {m} - ровно м раз
# {m,} - ровно м раз  и более
# {,m} - не более м раз
# {n,m} - от n раз до m раз - способ показать кол-во символов или подстрок

# import re
#
# pattern = r'\((.+?)\)' #  находим все что находится в скобках
# test_string = 'Поиск по образцу (pattern)!'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
#
# print(*result, sep='') # pattern

# import re
#
# pattern = 'o{2,5}' #  ПИШИМ БЕЗ ПРОБЕЛА
# test_string = 'Google, Gooogle, Goooooogle'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
#
# print(result) # ['oo', 'ooo', 'ooooo']

# import re
#
# pattern = 'Go{2,}gle' #  ПИШИМ БЕЗ ПРОБЕЛА
# test_string = 'Google, Gooogle, Goooooogle'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
#
# print(result) # ['Google', 'Gooogle', 'Goooooogle']

# import re
#
# pattern = 'Go{2,}gle' #  ПИШИМ БЕЗ ПРОБЕЛА
# test_string = 'Gogle, Gooogle, Goooooogle'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['Gooogle', 'Goooooogle']

# import re
# pattern = r'\+7\d{10}' #  ищем 10 дифр номер телефона
# test_string = 'Gogle: +78121234567'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['+78121234567']

# import re
# pattern = r'\+7\d{10}' #  ищем 10 дифр номер телефона
# test_string = 'Gogle: +78121234567'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['+78121234567']
#
# import re
# pattern = 'стеклянн?ый' #  будет искать искань н 1 или 2 последовательно
# test_string = 'стекляный, стекляный, оловянный, деревянный'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['стекляный', 'стекляный']

# import re
# pattern = '<img.*>' #  ищем все картинки с любым расширением
# test_string = 'Картинка в тексте <img src= "bg.jpg"> текст<\p>'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['<img src= "bg.jpg"> текст<\\p>']
#
# import re
# pattern = '<img.*?>' #  ищем все картинки с любым расширением
# test_string = 'Картинка в тексте <img src= "bg.jpg"> текст<\p>'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['<img src= "bg.jpg">']
#
# import re
# pattern = '<img[^>]+src="([^">]+)">' #  ищем все картинки с любым расширением
# test_string = 'Картинка в тексте <img src="bg.jpg"> текст<\p>'
# result = re.findall(pattern, test_string, re.I)  # re.I - игнорировать регистр
# print(result) # ['bg.jpg']
# http://regex101.com

#ДЕКАРАТОРЫ ФУНКЦИИ
#
# def wrapper():
#     def say_hello():
#         print('Hello')
#     say_hello()
# wrapper() # Hello
#
# def say_hello():
#     print('Hello')
#
# def higher_order(func):
#     func() # вызов функции, переданной в качестве параметра
# higher_order(say_hello)


# def say_hello():
#     print('Hello')
#
# def  decorator_function(func):
#     def wrapper():
#         print(f'Оборачиваемая функция {func}')
#         print('Выполняемая функция')
#         func()
#         print('выход из обертки')
#     return wrapper
#
# @decorator_function
# def say_hello():
#     print('Hello')
# say_hello()

# Оборачиваемая функция <function say_hello at 0x0000023C73C5E0D0>
# Выполняемая функция
# Hello
# выход из обертки

# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Затраченное время: {end-start} сек.')
#     return wrapper
#
# @benchmark
# def long_list_creactor():
#     a = [i for i in range(1000000)] # нужно создать список от 0 до 1000000
#
# long_list_creactor()
# # ОТВЕТ список из миллиона значений был создан за: Затраченное время: 0.045009613037109375 сек.
#
# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Затраченное время: {end-start} сек.')
#     return wrapper
#
# @benchmark
# def long_list_creactor():
#     a = list(i for i in range(1000000)) # нужно создать список от 0 до 1000000
#
# long_list_creactor()
# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Затраченное время: {end-start} сек.')
#     return wrapper
#
# @benchmark
# def long_list_creactor():
#     a = [i for i in range(1000000)] # нужно создать список от 0 до 1000000
#
# long_list_creactor()

# СЕТЕВОЕ ВЗАИМОДЕЙСТВИЕ

# from PIL import Image
#
# p = Image.open()
# p.mode # метод определят определение

# создание класса должны начинаться с заглавной буквы

class Fruit:    # создание класса
    pass


a = Fruit()      # создание экземпляр
b = Fruit()

print(type(a))  # <class '__main__.Fruit'>

