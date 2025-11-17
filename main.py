import os

clear = lambda: os.system('cls')

print('Привет! Я загадал слово. твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
clear()
print('Поехали!')

word = 'Stuttgart'

letters = []

while True:
    letter = input('Введите букву: ')
    letters.append(letter)
    print(letters)
    for symb in word:
        if symb in letters:
            print(symb, end= ' ')
        else:
            print('*', end=' ')
    print()