sz = "medvemancs"
e = 0
sz2 = ""
for c in sz:
    sz2 += c + "*"
    if c == "e" or c == "E":
        e = e + 1
if e > 0:
    print("Ebben a szövegben van e karakter van.")
else:
    print("Ebben a szövegben nincs e karakter van.")
print("Ebben a szövegben:", e ,"db e karakter van.")
print(sz2)



