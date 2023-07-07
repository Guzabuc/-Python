# import sqlite3
#
# подключаемся или создаем
# connection = sqlite3.connect('films_db.sqlite')
#
# # создать курсор
# cursor = connection.cursor()
# # вызываем запрос по доставке (fetchall) информации
# # fetchall - доставляет все полученные элементы
# result = cursor.execute("""Select * from films
# where year = ? and duration > ? """, (2009,)).fetchall()
# # ответ
# #(248, 'Алиса в стране чудес', 2010, 13, 201)
# #(4382, 'Железный человек 2', 2010, 11, 287)
# #(9138, 'Ноттингем', 2010, 11, 188)
# #(15495, 'Утомленные солнцем: Предстояние', 2010, 2, 139)
#
# # fetchone - доставляет только первый элемент
# # result = cursor.execute("""Select * from films
# # where year = 2010""").fetchone()
# # ОТвет
#
# # 248
# # Алиса в стране чудес
# # 2010
# # 13
# # 201
# # fetchmany(N) - доставляет только N элементов
# # result = cursor.execute("""Select * from films
# # where year = ? and duration > ?""", (2010, 90)).fetchmany()      # (2010, 90) можно указать параметры тут
# # (248, 'Алиса в стране чудес', 2010, 13, 201)
#
# print(f'найдено {len(result)} результатов')


# вывод на экран
# print()
#
# for item in result:
#     print(item)

# выходим из базы данных БД
# connection.close()



# import sqlite3
#
# connection = sqlite3.connect('films_db.sqlite')
# cursor = connection.cursor()
# result = cursor.execute("""Select * from films where year = ? and duration > ? """, (2009, 90)).fetchall()
# print(f'найдено {len(result)} результатов')
# connection.close()
# # найдено 90 результатов


# Запись в базу данных

# import sqlite3
# #  INSERT INTO <table_name> (id, name, surname, birthdate)
# connection = sqlite3.connect('films_db.sqlite')
# cursor = connection.cursor()
# result = cursor.execute("""insert into genres(id, title) values(26, 'басни')""").fetchall()
# # Запись в базу данных - подтверждение действий
# connection.commit()
# connection.close()


# import sqlite3
#
#
# connection = sqlite3.connect('films_db.sqlite')
# cursor = connection.cursor()
# # изменение запросов
# #  UPDATE - имя таблицы
# #  SET - название поля= значение
# #  Where - условие
#
# result = cursor.execute("""Update films Set duration = '283'
# where title = 'Аватар'""").fetchall()
# # Запись в базу данных - подтверждение действий
# connection.commit()
# connection.close()



# Удаление таблицы

# import sqlite3
#
#
# connection = sqlite3.connect('films_db.sqlite')
# cursor = connection.cursor()
#
# result = cursor.execute("""Delet films where duration = '283'""").fetchall()
# # Запись в базу данных - подтверждение действий
# connection.commit()
# connection.close()

# Создание БД

import sqlite3

connection = sqlite3.connect('shop.sqlite')
cursor = connection.cursor()

# cursor.execute("""Create table if not Exists users(
# userid int primary key,
# fname text,
# lname text,
# gender text);
# """)
#
# cursor.execute("""Create table if not Exists orders(
# orderid int primary key,
# date text,
# userid int,
# total int);
# """)
#
# cursor.execute("""insert into users(userid, fname, lname, gender)
# values(1, 'Alex', 'Smith', 'male')""")
#
# # user = (2, 'Lois', 'Griffin', 'femail')
# # cursor.execute("""insert into users Values(?, ?, ?,?)""", user)

# many_order = [
#     (4, '22.05.2022', '4', 3200),
#     (5, '02.04.2022', '2', 1500),
#     (6, '27.09.2022', '3', 1850)
# ]
# cursor.executemany("""insert into orders Values(?, ?, ?,?)""", many_order)

# result = cursor.execute("""
# select *  from orders
# where userid = (
# select userid from users where fname = 'Lois'
# )
# """).fetchall()
#
# result = cursor.execute("""
# select  sum(total) from orders
# where userid = (
# select userid from users where fname = 'Lois'
# )
# """).fetchall()

# result = cursor.execute("""
# select  users.fname, users.lname from orders
# left join users
# on users.userid=orders.userid
# """).fetchall()



# cursor.execute("""
# DELETE FROM orders
# WHERE userid=(
# select userid from users
# where fname like 'Lois'
# );
# """).fetchall()
#
# connection.commit()



# result = cursor.execute("""
# select fname, lname from users where userid = (select userid  from orders where total = 3200)
#
# """).fetchall()

# !!!!! Добавление данных по максимуму ид, то есть он будет заполнять автоматически его

# max_id = cursor.execute("""
# select max(userid) from users
# """).fetchone()
#
# res = cursor.execute(f"""
# insert into users values ({max_id[0] + 1}, 'KK', 'kk', 'll')""")

#  !!!!!! Обновление данных
cursor.execute(""" Update users set fname = 'Megg' where userid = (select userid from orders where total = 3200)

 """).fetchall()




connection.commit()
connection.close()