from tkinter import * # подключаем элементы tkinter
from tkinter import filedialog # для выбора картинки
from PIL import Image, ImageTk, ImageFilter, ImageEnhance # для обработки изображенияfro
from datetime import datetime
import os







class App():
    def __init__(self):
        self.window = Tk()   # Создали окно
        self.window.title('Обработка картинки')  # имя окна
        self.window.geometry('800x600')  # задаем размеры окна
        self.window.resizable(False, False) # изменять размеры окна нельзя ни по х ни по у
        self.window.iconphoto(False, PhotoImage(file='icons8.png'))

        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={name}&kind=metro&format=json'

        self.label = Label(text='Обработка изображений',
                           background='#ffff00', foreground='red',
                           font=('Verdana', 16))
        self.label.pack() # загрузили (упаковали label)
        self.canvas = Canvas(bg='white', width=600, height=400)   # создание холтса, где будет изображение
        self.canvas.pack(anchor=CENTER, pady=20)   # pady - отступ

        self.load = Button(text='Открыть', command=self.open) # создали кнопку
        self.load.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True) # padx=50 отсуп по оси х
        # anchor=N епляется к верхнему элементу, expand- размер кнопки будет меняться в завиимости от размера окна
        self.blur = Button(text='Размыть', command=self.blur)
        # создали кнопку c размытием
        self.blur.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True)
        self.sharp = Button(text='Резкость', command=self.sharp)
        # создали кнопку c размытием
        self.sharp.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True)
        self.dtime = Label(background='#ffffff', foreground='#111111',
                           font=('Verdana', 26))
        self.dtime.place(x=310, y=530)


        self.cwd = os.getcwd()

        self.image = None # заглушка (сюда будут поподать картинки)
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.show_time()
        self.window.mainloop() # ожидание (всегда на последней строчке)

    def open(self):
        try:
            fullpath = filedialog.askopenfilename(title='Выбор формата картинки',
                                                  initialdir=self.cwd,
                                                  filetypes= (
                                                      ('GIF', '*.gif'),
                                                      ('PNG', '*.png'),
                                                      ('JPG', '*.jpg')
                                                  )
                                                  )
            self.orig = Image.open(fullpath)
            self.w, self.h = self.orig.size
            mode = self.orig.mode
            if mode == 'P':    # если 256 color indexed image
                self.orig = self.orig.convert('RGB')
            if self.w > 600:
                ratio = self.w / 600
                self.orig = self.orig.resize((600, int(self.h/ratio)))
            if self.h > 400:
                ratio = self.h / 400
                self.orig = self.orig.resize((int(self.w/ratio), 400))
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:    # исключаем ошибку при незагрузки изображения
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def blur(self):
        blur_image = self.orig.filter(ImageFilter.BLUR)
        self.image = ImageTk.PhotoImage(blur_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.orig)
        sharp_img = sharper.enhance(5.0)   # 5.0 фактор резкосьти
        self.image= ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def show_time(self):
        self.time_to_show = datetime.time(datetime.now()).strftime("%H:%M:%S")
        self.dtime['text'] = self.time_to_show
        self.dtime.after(1000, self.show_time)
        # .after рекурсивный метод, каждую 1 секунду будет отображаться время




if __name__ == '__main__':
    app = App()

    # апускаем именно этот скрипт, его лучше не менять