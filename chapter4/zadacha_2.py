slovo = input('Напиши слово: ')
length = len(slovo)
word = ''

for i in range(length):
    word += slovo[length-i-1]

print(word)
