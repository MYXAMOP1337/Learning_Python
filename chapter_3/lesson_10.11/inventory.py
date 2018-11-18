def DisplayInventory(Inventory):
    print("Inventory:")
    for i in Inventory:
        print(str(Inventory[i]) + ' ' + i)

def AddToInventory(Inv,addedItems):
    for i in addedItems:
        if i in Inv:
          Inv[i] = Inv[i] + 1
    print("Inventory after dragon's death:")
    DisplayInventory(Inv)

data_1 = {"верёвка": 1, "фонарей": 6, "золотые монеты": 42, "кинжал": 1, "стрел": 12}

addedItems = {"золотые монеты", "вода", "кинжал", "вода", "магия"}

DisplayInventory(data_1)

AddToInventory(data_1, addedItems)
