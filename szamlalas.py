print("SZAMLALAS")

lista = [32, 5, 12, 8, 3, 75, 2, 15]
lista_2 = []
sz = 0
for number in lista:
    if number % 2 == 0:
        sz += 1
        lista_2.append(number)
print(sz)
print(lista_2)

print("HOSSZ")

names = ["Mark", "Tom", "Kate", "ANNABELLA"]
names_len = []
for number in names:
    names_len.append(len(number))
print(names_len)


