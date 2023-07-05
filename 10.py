# from lib import get_size, Fruit, Greeter
#
#
# a = Fruit()      # создание экземпляр класса
# b = Fruit()
#
# # print(type(a))  # <class '__main__.Fruit'>
# a.name = 'apple'
# a.weight = 120
#
# b.name = 'orange'
# b.weight = 220
# b.weight -= 10
#
# print(a.name, a.weight)
# print(b.name, b.weight) # orange 210
#
# c = Fruit()
# c.name = 'lemon'
# c.weight = 180
# c.color = 'yellow'
#
# print(c.name, c.weight, c.color)
#
# g = Greeter()
# g.say_hello()
# g.hello_name('Bob') # внутри скобок задали name
# g.hello_and_talk('Bob', 'Good Weather')
#
# get_size(a)
# get_size(b)
# get_size(c)
# get_size(g)
#
# # Размер: 32 байт(а)
# # Размер: 32 байт(а)

# from lib import get_size, Fruit, Greeter, Car
# # Инкапсуляция  - сокрытие данных от внешних изменений
# car = Car()
# car.start_engine()
# car.drive('работу')
#
# apple = Fruit('apple', 120, 'red')
# apple.color = 'green'
# apple.name = 'груша'   # нужно сделать так чтобы мы не могли поменять имя
# apple.get_info()

# свойство кода работать с разными действиями называется полиморфия
# print(1+1)
# print(0.5+1.8)
# print('17'+'15')
# 2
# 2.3
# 1715

# from lib import Book
#
# book = Book('Гроза', 'Островский')
# print(book.get_name()) # Гроза

# from lib import print_figure_info, Circle, Square, Rectangle
#
# square = Square(3)
# circle = Circle(5)
#
# print_figure_info(square)
# print_figure_info(circle)
#
# rectangle = Rectangle(2, 5)
# print_figure_info(rectangle)
#
# # class A:   - является базовым классом (родительским, либо суперкласс)
# #     pass
# #
# # class B(A):   частный случай от А (что умеет класс А, то умеет и В)
# #     pass        - классом В расширяем функионал класса А
# #                 (дочерним, унаследованным, производным)


from lib import print_figure_info , Triangle, EquilateralTriangle

treug = Triangle(1,2,3)
pr_treug = EquilateralTriangle(5)

print_figure_info(treug)
print_figure_info(pr_treug)


# гидхаб и openweather - зарегистрироваться
#
#
# openweather приходит код подтверждения
# после API - появиться API-key
#
#
#
#


