

lista = [32,5, 12, 8, 3, 75, 2, 15]
lista2 = ["aaa", "bbbb", "ccccccc"]
x = 0
sz = 0
sz2 = 0
while x < len(lista):
    sz +=lista[x]
    x += 1
print(sz)

# ez egyszerűbb:

for number in lista:
    sz2 +=number

print(sz2)

print("HOSSZ")

min = lista[0]
for number2 in lista:
    if number2 < min:
        min = number2
print(min)

print("MAX HOSSZ")

sz_min = len(lista2[0])

for number3 in lista2:
    if sz_min < len(number3):
        sz_min = len(number3)
print(sz_min)
