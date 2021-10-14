nevek = []
menu = 0
while menu != 3:
    menu = int(input("1. Új név rögzítése.\n" + "2. Nevek listája.\n" + "3. Kilép\n"))
    if menu == 1:
        nevek.append(input("név: "))
    else:
        print(nevek)
        menu = int(input("1. Új név rögzítése.\n" + "2. Nevek listája.\n" + "3. Kilép\n"))
print("VÉGE")


