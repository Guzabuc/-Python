# import turtle as t
#
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.mainloop()

# import turtle as t
#
# counter = 0
# while counter < 4:
#     t.forward(200)
#     t.right(90)
#     counter += 1
# t.mainloop() # ожидание действий

# import turtle as t
#
# t.speed(10)
#
# counter = 5
# dist = 200
# angel = 360 / counter
# t.goto(-100,100) # смещение оси
#
# t.color('red')
# t.width(5)
#
# while counter > 0:
#     # t.forward(dist)
#     # t.circle(dist)
#     sides = 0
#     while sides < 4:
#         t.forward(dist)
#         t.left(90)
#         sides += 1
#     t.right(angel)
#     counter -= 1
# t.mainloop() # ожидание действий

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# python_group = ['яблоко', 'кофе']
#
# print(type)
#
# python_group += ['груша']
# python_group[0] = 'булка'
# count = len(python_group)
# print('В списке:', count, 'чел.')
#
# counter = 0
#
# while counter < count:
#     print(str(counter + 1) + '-', python_group[counter],
#           end='. ')
#     counter += 1
#
#
# print()
# print(*python_group, sep= ', ')
# string = 'python'
# print(*string, sep='-')

# python_group = ['яблоко', 'кофе', 'груша', 'шоколад']
#
# count = len(python_group)
#
# # for item in python_group:
# #     print(item)
#
# for i in range(0, count, 2):
#     print(python_group[i])

# python_group = ['яблоко', 'кофе', 'груша', 'шоколад']
#
# count = len(python_group)
# index = python_group.index('кофе')
#
# print('кофе на', index, 'месте')

# a = []
# for i in range(51):
#     # a += [i] - первый способ (сложение списков)
#     a.append(i) - добавление к концу списка
# print(*a)

# stack = []
#
# for i in range(5):
#     stack.append(input('Кладем число ' + str(i + 1) + ' в строку: '))
# while stack:    # пока стек не пуст
#     print('Из стопки уходит', stack.pop())

# def greeting(name= 'noname'):
#     print('Привет,', str(name) + '!')
#
#
# names = ['николай', 'дмитрий', 'петр']
# for name in names:
#     greeting(name)

# counter = 0
#
# def greeting(name='noname'):
#      print('Привет,', str(name) + '!')
#
#
# def increment_counetr():
#    global counter
#    counter += 1
#
# print('до', counter)
# increment_counetr()
# print('после', counter)
#
# names = ['николай', 'дмитрий', 'петр']
# for name in names:
#     greeting(name)

counter = 0

def summ(a, b):
    return a + b

# res = summ(5,5) - первый способ вывода суммы 5+5
# print(res)
print(summ(5,5)) # - второй способ выводв суммы 5+5
