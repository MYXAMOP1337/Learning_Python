import random

print('Добро пожаловать в игру "Отгадай число"')
print('Я загадал натуральное число от 1 до 100')
print('Постарайтесь отгадать его за минимальное количество попыток')
the_number = random.randint(1, 100)
guess = int(input('Ваше предположение: '))
tries = 1

while guess != the_number:
    if guess > the_number:
        print('Меньше...')
    else:
        print('Больше...')

    guess = int(input('Ваше предположение: '))
    tries += 1

print('Вам удалось отгадать число! Это в самом деле', the_number)
print('Вы затратили на угадывание лишь', tries, "попыток")
