alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

privet = 'привет это я, а может и не я'

bias = 3
code = []

for i in privet:
    if i.isalpha():
        index = alphabet.index(i.upper())
        i_code = index + bias

        if i_code > len(alphabet):
            i_code -= len(alphabet)
            i_code = alphabet[i_code]
            code.append(i_code)

        elif i_code <= (len(alphabet) - 1):
            i_code = alphabet[i_code]
            code.append(i_code)
    else:
        code.append(i)
print('Закодированная строка: ', ''.join(code).lower())
