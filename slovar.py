slovar = {
    'hi': 'привет',
    'hello': 'привет',
    'noon': 'настроение',
    'charge': 'заряжать',
    'chase': 'приследовать',
    'adjust': 'управлять'
    }

input_eng = input('Введите слово для перевода с анг -> на рус: ').lower()

if input_eng in slovar.keys():
   print (f'Перевод слова {input_eng} -> {slovar[input_eng]}' )
else:
   print('Такого слова нет.\n\
         Хотите ли вы его сохранить? (Да/Нет)')
   answer = input().lower()
   if answer == 'да':
      print('Введите значение слова:')
      new_value = input().lower()
      slovar[input_eng] = new_value
      print(f'Слово добавлено: {input_eng} -> {new_value}')
   else:
      print('Как хотите.') 
print(slovar)

      


