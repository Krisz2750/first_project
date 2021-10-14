def print_function():
    print("HELLO FUNCTIONS!")


def szumma(number_a, number_b):
    szam = number_a+number_b
    return szam


def szoveg(szoveg_2):
    i = 0
    for c in szoveg_2:
        if c == " ":
            i += 1
    print(i)


def atlag(lista):
    a = 0
    for number in lista:
        a += number
    return a / len(lista)



print_function()
szumma(5, 6)
szoveg("me nnyi az annyi? ")
lista = [2, 3, 4, 5, 6]
print(atlag(lista))