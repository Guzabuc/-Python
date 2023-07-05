# n = int(input('Введите целое число: '))
#
# if n % 2 == 0:
#     print('Число', n, 'четное.')
# else:
#     print('Число', n, 'нечетное.')

# for n in range(101):
#     if n % 10 == 7:
#         print(n)

# print("""Налево пойдешь - женишься,
# направо пойдешь - коня потеряешь,
# прямо пойдешь - смерть свою найдешь.
# Прямо  - f, Налево - l, Направо - r.""")
#
# while True:
#     choice = input('\nКуда пойдем?: ')
#     if choice == 'r':
#         print('Ваш конь Вам больше не доверяет!')
#         break
#     elif choice == 'l':
#         print('Кольцо всевластия сжимает ваш палец!')
#         break
#     elif choice == 'f':
#         print('Вы катаетесь на велосипеде по ромашковому полю!')
#         break
#     else:
#         print('Направление не определено!')

# correct_pass = 'kkk'
# attempts = 3
# counter = 0

# while True:
#     pwd = input('\nВведите пароль!: ')
#     if pwd == correct_pass:
#         print('Доступ разрешен.')
#         break
#     else:
#         attempts -= 1
#         print('Пароль неверный', end=', ')
#         if attempts  == 0:
#             print('доступа нет ', end=',')
#             print('попыток no')
#             break

# correct_pass = 'kkk'
# attempts = 3
# counter = 0
#
# while counter < attempts:
#     pwd = input('\nВведите пароль!: ')
#     if pwd == correct_pass:
#         print('Доступ разрешен.')
#         break
#     else:
#         attempts -= 1
#         print('Пароль неверный', end=', ')
#         print( 'сталось ', attempts)
#         if attempts  == 0:
#             print('доступа нет ', end=',')
#             print('попыток не осталось')
#             break

# def divider(a, b):
#     if b != 0:
#         return a / b
#     return 'ошибка, деления на ноль'
#
# a = 3
# b = 0
#
# print(divider(a, b))
# - считаем факториал

# def factorial1(n):
#     x = 1
#     for i in range(1, n+1):
#         x *= i
#     return  x
# print(factorial1(5))

# def factorial_r(n):
#   if n == 0:
#       return 1
#   return n * factorial_r(n - 1)
#
# print(factorial_r(5)) # т.е у нас есть n=5, его умножаем 5 * 4 *3 * 2 * 1 * 1(0-заменяется на 1) и заканчивается цикл
# c 8 до 12 - доброе утро
# с 12 до 18 - добрый день
# с 18 до 22 - добрый вечер
# во всех остальных случаях - доброй ночи

# первый вариант
# def greeting(hour):
#
#     if hour >= 8 and hour< 12:
#         print('доброе утро')
#     elif hour >= 12 and hour< 18:
#         print('добрый день')
#     elif hour >= 18 and hour< 22:
#         print('добрый вечер')
#     else:
#         print('доброй ночи')
#
# for h in range (24): # - 'это тестировщик на все параметры времени
#     print('на часах', h, end=': ')
#     greeting(h)
# второй вариант
# def greeting(hour):
#     if 8 <= hour < 12:
#         print('доброе утро')
#     elif 12 <= hour < 18:
#         print('добрый день')
#     elif 18 <= hour < 22:
#         print('добрый вечер')
#     else:
#         print('доброй ночи')
#
#
# for h in range(24):  # - 'это тестировщик на все параметры времени
#     print('на часах', h, end=': ')
#     greeting(h)

# step_yest = 32500  # шаги за вчера
# step_today = 5500  # шаги за сегодня
#
# str_out = 'Вы прошли '
#
# steps_sum = step_yest + step_today # сумма шагов
#
# if steps_sum >= 10000:
#     gygees = steps_sum // 10000 # читаем сколько гб он получил за шаги
#     str_out += str(steps_sum)+' шагов. Поздравляем! '
#     str_out += ' \nТеперь вам доступно ' + str(gygees) +'Гб.'
#     str_out += ' \nдо следующего Гб вам осталось пройти  '
#     str_out += str(10000 * gygees -(steps_sum -10000))
#     str_out += ' шагов.'
# else:
#     str_out += ' пока что только '
#     str_out += str(steps_sum)
#     str_out += ' шагов. Есть к чему стремиться. '
#     str_out += '\nДля получения 1Гб Вам нужно пройти еще '
#     str_out += str(10000-steps_sum) + ' шагов.'
# print(str_out)

# from datetime import datetime
#
# get_time = datetime.time(datetime.now())
# cur_time = get_time.strftime("%H:%M") # переводит 14:47:00.968558 в читабельный вид 14:51
# hour = int(get_time.strftime("%H")) # переводим значение строки в число и берем только час
# # либо можно убрать переменную get_time и прописать все в одной строке
#
# print('На часах:', cur_time)
# # c 8 до 12 - доброе утро
# # с 12 до 18 - добрый день
# # с 18 до 22 - добрый вечер
# # во всех остальных случаях - доброй ночи
#
# def greeting(hour):
#
#     if hour >= 8 and hour< 12:
#         return 'доброе утро'
#     elif hour >= 12 and hour< 18:
#         return'добрый день'
#     elif hour >= 18 and hour< 22:
#         return'добрый вечер'
#     else:
#         return'доброй ночи'
#
# print(greeting(hour))

# color = input('Цвет шарика: ')
#
# if color == 'зеленый' or color == 'синий':  # хотя бы одно совпадение должно быть.
#     print('эти шары подойдут')
# else:
#     print('не годится')

# нужно сдлать узор из прямых линий с поворотами

# import turtle as t
#
# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
# n = 6
# angle = 200 # (360 / n - 1)  # - будет спираль
#
# if n > 6: # что бы не превышало кол-во сторон 6 , если нужно
#     n = 6
#
# t.speed(0)
# t.bgcolor('black')     # задаем фон
#
# for x in range(201):
#     t.pencolor(colors[x % n])
# # статок от деления на шесть (так как шагов 200, а у нас всего только 6 цветов, т.о
# # он будет возращаться к началу списка и начинать с начала списка
#     t.width(x // 50 + 1) # получается воронка
#     t.forward(x)
#     t.left(angle)
#
# t.mainloop()   # чтобы после прорисовки узора не закрылся сразу

# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
#
# # print(colors[-2])   # отрицательные индексы идут с конца списка
# # print(colors[0:6:2]) # Ex среза [0:3] первые три  or [3:6] - последние три, [0:6:2] - из все с шагом 2
# print(colors[::-1]) # если не указаны числа они идут стандарно начало с 0, весь список, после идет шаг
# string = 'python'
# print(string[::-1])

# wrd = input('Введите слово: ')
#
# if wrd == wrd[::-1]:
#     print(wrd, 'молодец, это палиндром')
# else:
#     print(wrd, 'это не палиндром')

num = input('ведите число: ')
a =0
for i in num:
    a += int(i)
print('сумма разрядов числа', num, '=', a)
