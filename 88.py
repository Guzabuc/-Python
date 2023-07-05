import pickle

f = open('dictinary.bin', 'rb')
d = pickle.load(f)


while True:
    word = input('Введите слово для перевода (или QQ - для выхода): ')
    if word == 'QQ':
        break
    if word in d:
        print(f'Перевод слова: {word} -> {d[word]}')
    else:
        print('Я не знаю этого слова, но можете мне подсказать:')
        new_word = input(f'Как переводится {word}: ')
        d[word] = new_word
        g = open('dictinary.bin', 'wb')
        pickle.dump(d, g)
        g.close()

# with open('dictinary.bin', 'wb') as f:
#     pickle.dump(d, f)
#     f.close()
# print('Спасибо, до свидания')