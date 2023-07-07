import random
import time
import sqlite3
from random import randrange
import numpy as np  # used in date generation (for orders)
from faker import Faker  # fake data library


def str_time_prop(start, end, time_format, prop):  # random date generator (for orders
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m.%d.%Y', prop)


# connecting to the database
filename = 'shop.sqlite'
connection = sqlite3.connect(filename)

# creating the cursor
cursor = connection.cursor()

fake = Faker('en_US')


def name_gen(start, end):  # name generation
    for _ in range(start, end):
        gender = np.random.choice(['male', 'female'], p=[0.5, 0.5])
        if gender == 'male':
            firstname = fake.first_name_male()
            lastname = fake.last_name_male()
            rnd_female_name = f"INSERT INTO users VALUES ({_}, '{firstname}', '{lastname}', '{gender}')"
            print(rnd_female_name)
            # cursor.execute(rnd_female_name)
        else:
            firstname = fake.first_name_female()
            lastname = fake.last_name_female()
            rnd_male_name = f"INSERT INTO users VALUES ({_}, '{firstname}', '{lastname}', '{gender}')"
            print(rnd_male_name)
            # cursor.execute(rnd_male_name)


def order_gen(start, end):  # order generation
    for _ in range(start, end):
        rnd_daterange = random_date("1.1.2019", "1.1.2023", random.random())  # setting up range for date generation
        rnd_order_value = f"INSERT INTO orders VALUES ({_}, '{rnd_daterange}', {randrange(1, 9)}, {random.randrange(100, 5000, 100)})"
        print(rnd_order_value)
        cursor.execute(rnd_order_value)


# name_gen(1, 1001)
order_gen(1, 1001)

connection.commit()

connection.close()