

lista = [32,5, 12, 8, 3, 75, 2, 15]
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

