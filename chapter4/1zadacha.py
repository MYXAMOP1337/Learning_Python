print('Привет, я буду считать за тебя.')
first = int(input('Напиши первое число: '))
last = int(input('и последнее: '))
gap = int(input('и интервал, если возможно: '))
for i in range(first, last + 1, gap):
    print(i, end=' ')
input("\nНажми Enter, чтобы выйти")
