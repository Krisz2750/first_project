
szamok=[]
szamok = [input("Adj meg 5 számot  -1 és 10- között!")]
print("Ezeket a számokat adtad meg:", szamok)
max_szam = szamok[0]
for number in szamok:
    if max_szam < number:
        max_szam = number

print("Max szam:", max_szam)


