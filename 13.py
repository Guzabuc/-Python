from tkinter import * # подключаем элементы tkinter
from tkinter import filedialog # для выбора картинки
from PIL import Image, ImageTk, ImageFilter, ImageEnhance # для обработки изображенияfro
from datetime import datetime
import os
import requests
from io import BytesIO



class App():
    def __init__(self):
        self.window = Tk()   # Создали окно
        self.window.title('Поиск по карте')  # имя окна
        self.window.geometry('800x600')  # задаем размеры окна
        self.window.resizable(False, False) # изменять размеры окна нельзя ни по х ни по у
        self.window.iconphoto(False, PhotoImage(file='icons8.png'))

        self.name = 'Санкт-Петербург, ул. Можайская 2'
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}&kind=metro&format=json'

        self.label = Label(text='Поиск по карте',
                           background='#ffff00', foreground='red',
                           font=('Verdana', 16))
        self.label.pack() # загрузили (упаковали label)

        self.canvas = Canvas(bg='white', width=600, height=450)   # создание холтса, где будет изображение
        self.canvas.pack(anchor=CENTER, pady=20)   # pad - отступ

        self.load = Button(text='Найти', command=self.open) # создали кнопку
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True) # padx=50 отсуп по оси х
        self.place = Entry(width=60, font=('Verdana', 16))
        self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)





        self.cwd = os.getcwd()

        self.image = None # заглушка (сюда будут поподать картинки)
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        # self.show_time()
        self.window.mainloop() # ожидание (всегда на последней строчке)

    def open(self):
        self.name = self.place.get()
        if self.name == '' or len(self.name) < 5:
            self.name = 'Санкт-Петербург, ул. Можайская 2'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}&kind=metro&format=json'
        response = requests.get(self.geocoder_request)   # response - ссылка на объект
        info = response.json()
        coords = info['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

        # 30.325498 59.918305 нам нужно записать координаты через запятую
        coords = ','.join(coords.split())
        delta = '0.005,0.005'
        # отступ
        # обираем параметры для запроса static-maps
        # создаем словарь
        map_param = {
            'll': coords,
            'spn': delta,
            'l': 'map',
            'pt': f'{coords},pm2dgl'
        }
        api_server = 'http://static-maps.yandex.ru/1.x/'
        image_map = requests.get(api_server, params=map_param)
        # получили массив пикселей  проверка print(image_map)  <Response [200]>
        pick_to_show = Image.open(BytesIO(image_map.content))
        self.image = ImageTk.PhotoImage(pick_to_show)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

if __name__ == '__main__':
    app = App()

    # апускаем именно этот скрипт, его лучше не менять