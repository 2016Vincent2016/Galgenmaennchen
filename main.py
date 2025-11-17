import os

clear = lambda: os.system('cls')

print('Привет! Я загадал слово. твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
clear()
print('Поехали!')

word = 'Stuttgart'

for symb in word:
    print(symb, end= ' ')


