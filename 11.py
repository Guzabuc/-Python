# from lib import Car
# a = Car()
# b = Car()
# c = Car()
#
# b.start_engine()
# b.drive('работу')
#
# print(Car.drive)
#
# print(Car.get_count)

# from lib import List
#
# l = List('jjjjjjjj')
# l.show_list()
# l.clear()
# l.show_list()

# from lib import Special
#
# s = Special() # Вызвали класс
# print(s)
# print(s+1)
# print(1+s)
# s += 1  # переназначаем действия оператора
# print(s)

# from lib import Time
# t1 = Time(10, 50) # 10 - минут, 20- секунд
# t2 = Time(8, 40)
#
# t3 = [t1, t2] # ВЫводит инфу в удобном для нас ввиде
# print(t3)
#
# t3 = t1 +t2
# # t3 = t1 +t2 t1.__add__(t2)
# # print(t3.info()) 19: 30
# print(t3) #  он преобразовывает объкт t3 в строку с содержание t1 +t2, str(t3) ->t3.__str___()
#
#
# from lib import Rectangle
#
# rect1 = Rectangle(10,20)
# rect2 = Rectangle(110,20)
#
# # ы сравниваем равни ли они между собой (больше меньше или равно)
#
# print(rect1 == rect2)

# графическое отображение


from tkinter import *   # GUI - графическиq интерфейс пользователя, tkinter не работает
from  PIL import Image, ImageTk
# пишем функцию для кнопки при нажатии

from lib import Okno

if __name__ == '__main__':

    app = Okno()


# comment