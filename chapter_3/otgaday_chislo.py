import random

print('Добро пожаловать в игру "Отгадай число"')
print('Я загадал натуральное число от 1 до 100')
print('Постарайтесь отгадать его за 3 попытки')
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

    if guess > the_number and tries >= 6:
        print("Ну, для школы восьмого типа ты вполне умён")
    elif guess < the_number and tries >= 6:
        print("Азаза, моя бабушка отгадывает числа лучше")

print('Вам удалось отгадать число! Это в самом деле', the_number)
print('Вы затратили на угадывание лишь', tries, "попыток")
if tries >= 6:
    print(tries,'попытки(ок), ты гениален(нет)')
