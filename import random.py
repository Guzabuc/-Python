import random

game = True
attempt = 1
difficult_dict =  {
        'легкий': 9,
        'средний': 30,
        'сложный': 100
        }


def guess_number(difficult):
    return random.randint(0, difficult_dict[difficult])

def advice(difficult):
    if difficult == 'средний':
        print('Еще не придумано!')
    elif difficult == 'сложный':
        print('Обойдешься!!! Сам мучайся!')
    else:
        print('Совета не будет')


while game:
    print ('Вы хотите поиграть в Угадай число?')
    ask = input('(да/нет): ').lower()
    if ask == 'да':
        print ('Есть три варианта сложности! \n\
                    Легкий\n\
                    Средний\n\
                    Сложный\n\
            Какой выберете ВЫ?!')
        difficult = input ('(Легкий/Cредний/Сложный): ').lower()
        num = guess_number(difficult)
    else:
        print ('Вы не хотите со мной играть...')
        game = False
        break

    print ()
    print('Игра Угадай число началась!!!')
    print (f'Вам нужно угадать число от 0 до {difficult_dict[difficult]}')
    print ('Если нужен совет, то напишите "помощь"')

    while game:
        m_num = input('Введи свое число: ').lower()
        
        if m_num.isdigit():
            m_num = int (m_num)
            if m_num == num:
                print('Вы угадали число!')
                print ('Число попыток:', attempt)
                break

            elif m_num > num:
                print('Ваше число больше загаданного')

            elif m_num < num:
                print('Ваше число меньше загаданного')
        
        elif m_num.isalpha() and m_num == 'помощь':
            advice(difficult) 
            print ('Но попытка засчитана, Хи-Хи')

        attempt += 1
            
    print('Загаданное число:', num)