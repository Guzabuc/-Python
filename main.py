a = float(input('сколько стоил пончик: '))
b = float(input('сколько стоил кофе: '))
с = 'Ура! '
print('я потратил ', a + b)
print(с*3)
num = 56
print('Козерог-' + str(num))
string = 'мы прошли'
steps = input('сколько вы прошли: ')
res = string + ' ' + steps + ' шаг(ов).'
print(res)

import math

r = float(input('ведите радиус круга: '))
c = 2 * math.pi * r
a = math.pi * math.pow(r, 2)
print('длина круга:', round(c, 2))
print('площадь круга:', round(a, 2))
