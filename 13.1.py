# csv - comma seperated valves

import csv

# with open('sq.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#
#     delimiter = ';'
#     for i in range(10):
#         writer.writerow([i, i ** 2, f' Квадрат числа {i} = {i ** 2}'])

        # encoding='utf-8' в питоне будет читаться, но в экселе неправильно отобразится. ее лучше убрать.
        # writer = название переменной, .writer - метод
        # 'w' если поставить r будет зависыват

# with open('sq.csv', 'r', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=';', quotechar='"')
#     for i in reader:
#         x, y, z = i
#         print(x, y, z )

# goods = (['Товар', 'Цена'], ['ковер', '100'], ['Утюг', '200'], ['Пенал', '300'])
# with open('goods.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     for i in goods:
#         writer.writerow(i)
#         print(i)

data = [{
    'lastname': 'Кузнецов',
    'fname': 'Петр',
    'class_num': '9',
    'class_letter': 'А'
},
    {
        'lastname': 'Меньшов',
        'fname': 'Алексей',
        'class_num': '9',
        'class_letter': 'Б'
    }
]
# with open('form.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
#                             delimiter=';', quoting=csv.QUOTE_NONNUMERIC)   # имена полей fieldnames
#     writer.writeheader()
#     for i in data:
#         writer.writerow(i)

with open('form.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

    for item in reader:
        for k, v in item.items():
            print(k, v)
