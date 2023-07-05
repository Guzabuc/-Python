from tkinter import *   # GUI - графическиq интерфейс пользователя, tkinter не работает
from  PIL import Image, ImageTk
from tkinter import filedialog


def div(a, b):
    if b != 0:
        print(f'{a / b:.1f}')
    else:
        print('на 0 делить нельзя')

print(__name__)

def get_size(obj):
    print(f'Размер: {obj.__sizeof__()} байт(а)')

# __sizeof__ - метод, определяет размер файла

class Car:

    count = 1
    def __init__(self):
        self.engine_on = False  # пока не заведен
        Car.count += 1 # увеличиваем на 1

    def start_engine(self):
        self.engine_on = True  # завели

    def drive(self, place):
        if self.engine_on:
            print(f'Еду на {place}')
        else:
            print('Забыл завести мотор')
    @staticmethod
    def get_count():
        return Car.count



class Fruit:    # создание класса
    def __init__(self, name, weight, color):
        self.__name = name   # __name параметр менять нельзя (но он не работает),
        # таким образом мы показываем что его нельзя изменять для других
        self.weight = weight
        self.color = color

    def set_color(self, new_color, new_weight): # setter  даем разрешение на изменение информации
        self.color = new_color
        self.weight = new_weight

    def get_color(self):    # getter (метод) даем разрешение на получение информации
        return self.color

    def get_info(self):
        print(f'{self.name}',f' {self.weight} гр.', f'{self.color} ')



class Greeter:
    def say_hello(self):  # self ссылка на который ссылается объект, в нашем случае это g
        print('Hello')

    def hello_name(self, name):
        print(f' Hello, {name}')

    def hello_and_talk(self, name, weather):
        print(f'Hello, {name}')
        print(f'{name}, {weather}')

# свойство кода ратать с разными называется полиморфия

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def get_name(self):
        return self.name
    def set_author(self, new_author):
        self.author = new_author


from math import pi


def print_figure_info(figure):


    if isinstance(figure, Circle):   # вытаскиваем Имя класса
        print('для Круга')
    elif isinstance(figure, Square):
        print('для Квадрата')
    elif isinstance(figure, Rectangle):
        print('для Прямоугольника')
    elif isinstance(figure, EquilateralTriangle):
        print('для Правельного Треугольник')
    elif isinstance(figure, Triangle):
        print('для Треугольника' )




    # o_type = type(figure).__name__  # вытаскиваем Имя класса
    # if o_type == 'Circle':
    #     print('для Круга')
    # elif o_type == 'Square':
    #     print('для Квадрата')
    # elif o_type == 'Rectangle':
    #     print('для Прямоугольнике')
    print(f'\tArea = {figure.area():.1f}\n\tPerimetr = {figure.perimetr():.1f}')
    # :.1f - выводит 1 знак после запятой


# и в конце получаем пример для квадрата
# для Квадрата
# Area = 25
# Perimetr = 20

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'Круг'

    def area(self):
        return pi * self.radius ** 2

    def perimetr(self):
        return 2 * pi * self.radius




class Rectangle:
    def __init__(self, side_1, side_2):
        self.a = side_1
        self.b = side_2


    def area(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a + self.b)*2

# Операторы сравнения
    # __eq__() – для равенства ==
    # __ne__() – для неравенства !=
    # __lt__() – для оператора меньше <
    # __le__() – для оператора меньше или равно <=
    # __gt__() – для оператора больше >
    # __ge__() – для оператора больше или равно >=


    def __eq__(self, other):      # __eq__ - равно
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.a >= other.a and self.b >= other.b:
            return True
        else:
            return False

    def __ne__(self, other):
        return 'меня вызвали'

    def __lt__(self, other):
        print('вызван меньше чем')


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
# class Square:
#     def __init__(self, side):

    # def area(self):
    #     return self.side ** 2
    #
    # def perimetr(self):
    #     return self.side * 4
# обстракция работа с методами,  не вникая как выглядит там.
#self.a - публичный (public)
#self._a - защищенный (protected)
#self.__a - приватный, закрытый (private)


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.a = side_1
        self.b = side_2
        self.c = side_3

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        return 0

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.side = side


# добавить, удалить, очистить
class List:
    def __init__(self, n=0):
        if n == 0:
            self.a = []
        else:
            try:                # обрабатываем исключение
                n = int(n)
                n = abs(n)
                self.a = [0 for i in range(n)]
            except ValueError:
                self.a = []

    def add(self, value=''):
        self.a.append(value)

    def clear(self, value=''):
        self.a.clear()


    def remove(self, value):
        try:
            self.a.remove(value)
        except:
            print('Элемента нет в списке')

    def show_list(self):
        print(*self.a, sep=', ')

# спецметоды перегрузка(переназначение действий) оператора

class Special:

    def __init__(self):
        self.value = 10

    def __add__(self, other): # s+1 - прибавление к списку слева
        return 'Выполнился __add__'

    def __radd__(self, other): # 1+s - прибавление к списку справа
        return 'Выполнился __radd__'

    def __iadd__(self, other): # s += 1 сложение с присваиванием, оператор
        self.value += other
        print('Выполнился __iadd__')
        return self

    def __str__(self): # перобразовать в строку
        return f'Значение {self.value}'

class Time:

    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.minutes:02d}: {self.seconds:02d}'

    def __repr__(self):
        return f'{self.minutes:02d}: {self.seconds:02d}'

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s //60 # тобы не превысело 60, так как это время
        s = s % 60
        return Time(m, s)


# a = str(b) x.__str__()


class Okno:

    def __init__(self):
        self.window = Tk()
        self.window.title('Добро пожаловать в tkinter ')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        # .resizable(False, True) ограничавает действие с изменением окна, тоесть здесь нельзя поменять по оси х, но можно по оси у
        self.lbl = Label(self.window, text='Картинка ниже')
        self.lbl.pack()
        # добавляем изображение
        self.canvas = Canvas(self.window, height=100, width=100)
        # Вставляем картинку 2 способа

        # 1 способ для всех форматов (включая jpeg)
        # file= Image.open('images/image.png')
        # image= ImageTk.PhotoImage(file)

        # 2 способ только png
        self.image = PhotoImage(file='images/image.png')  # только ждя формата png

        self.canvas.create_image(0, 0, anchor='nw',
                                 image=self.image)  # anchor='nw',- размещается с левого верхнего угла
        self.canvas.pack()

        # добавляем кнопку и задаем координаты .pack()
        self.btn = Button(self.window, text='Нажми', command=self.click)
        self.btn.pack()
        self.window.mainloop()

    def click(self):  # при нажатии на кнопку
        path = filedialog.askopenfilename()
        original = Image.open(path)
        w, h = original.size
        ratio = w/ 100
        if w > 100:
            original.resize((100, int(h / ratio)))

        self.image = ImageTk.PhotoImage(original)
        # self.image = PhotoImage(file='images/image1.png') # Было
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)


# БЫЛО СОЗДАНО РАНЕЕ НО СЕЙЧАС НЕ РАБОТАЕТ
#
#         def rgb(r=0, g=0, b=0):  # задаем стандартный цвет - БЫЛО СОЗДАНО РАНЕЕ НО СЕЙЧАС НЕ РАБОТАЕТ
#             return f'#{r:02x}{g:02x}{b:02x}'
#
#         global status
#         if not status:
#             # изменяем текс на метке
#             self.lbl['text'] = 'Нажми'
#             self.lbl['background'] = rgb(255, 0, 0)
#             self.btn['text'] = 'Нажми'
#             self.btn['background'] = '#ff00ff'
#         else:
#             self.lbl['text'] = 'Кнопка нажата'
#             self.lbl['background'] = self.window.cget('bg')  # .cget получить системный фон(background)
#             self.btn['text'] = 'Меня нажали'
#             self.btn['background'] = self.window.cget('bg')
#         status = not status  # инверсия


from tkinter import  * # подключаем элементы tkinter
from tkinter import filedialog # для выбора картинки
from PIL import Image # для обработки изображения

class App:
    def __init__(self):
        self.window = Tk()   # Создали окно
        self.window.title('Обработка картинки') # имя окна
        self.window.geometry('800x600') # задаем размеры окна
        self.window.resizable(False, False) # изменять размеры окна нельзя ни по х ни по у
        self.window.mainloop()

