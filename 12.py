from tkinter import  * # подключаем элементы tkinter
from tkinter import filedialog # для выбора картинки
from PIL import Image, ImageTk # для обработки изображения

class App():
    def __init__(self):
        self.window = Tk()   # Создали окно
        self.window.title('Обработка картинки')  # имя окна
        self.window.geometry('800x600')  # задаем размеры окна
        self.window.resizable(False, False) # изменять размеры окна нельзя ни по х ни по у
        self.window.iconphoto(False, PhotoImage(file='icons8.png'))
        self.label = Label(text='Обработка изображений',
                           background='#ffff00', foreground='red',
                           font=('Verdana', 16))
        self.label.pack() # загрузили (упаковали label)
        self.canvas = Canvas(bg='white', width=600, height=400)   # создание холтса, где будет изображение
        self.canvas.pack(anchor=CENTER, pady=20)   # pady - отступ

        self.load = Button(text='Открыть', command=self.open) # создали кнопку
        self.load.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True) # padx=50 отсуп по оси х
        # anchor=N епляется к верхнему элементу, expand- размер кнопки будет меняться в завиимости от размера окна
        self.load = Button(text='Размыть')  # создали кнопку
        self.load.pack(anchor=N, side=LEFT, padx=50, fill=X, expand=True)
        self.image = None # заглушка (сюда будут поподать картинки)
        self.orig = Image.new('RGB', (600, 400), (255, 255, 255))

        self.window.mainloop() # ожидание (всегда на последней строчке)

    def open(self):
        try:
            fullpath = filedialog.askopenfilename()
            self.orig = Image.open(fullpath)
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

        except AttributeError:    # исключаем ошибку при незагрузки изображения
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)


if __name__ == '__main__':
    app = App()

    # апускаем именно этот скрипт, его лучше не менять