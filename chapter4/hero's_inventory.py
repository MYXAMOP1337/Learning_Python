# Арсенал героя
# Демонстрирует создание кортежа
# создадим пустой кортеж
inventory = ()
# рассмотрим его как условие
if not inventory:
    print("Вы безоружны.")
input("\nНажмите Enter, чтобы выйти")
# теперь создадим кортеж с несколькими элементами
inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
# выведем этот кортеж на экран
print("\nСодержимое кортежа:")
print(inventory)
# выведем ве элементы последовательно
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\n\nНажмите Enter, чтобы выйти")
