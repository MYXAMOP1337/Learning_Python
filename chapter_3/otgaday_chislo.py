print("\t\t\tЗдравствуй, игрок!")
print("Тебе предстоить сыграть с компьютером в 'Числа'.")
print("Надо загадать число от 1 до 100, а компьютер попытается отгадать его.")
number = int(input("Введите загаданное число: "))

computer_number = 50
tries = 1
low = 1
high = 100
print(computer_number)


while computer_number != number:
    if computer_number > number:
        high = computer_number
    else:
        low = computer_number

    computer_number = low + (high - low) // 2

    print(computer_number)

    tries += 1

print("Компьютер потратил", tries, "попытки(ок) на отгадывание твоего числа.")
input("\n\nНажмите Enter, чтобы выйти из программы...")