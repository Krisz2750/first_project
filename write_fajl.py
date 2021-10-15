from os.path import exists

print(isfile(numbers.txt))
print(isfile(numbers_eee.txt))


with open ("numbers.txt", encoding="utf-8", mode="w") as f:
    for i in range(10):
        f.write(f"Szam: {i}\n")

with open("numbers.txt", encoding="utf-8", mode="a") as f:
    for i in range(10):
        f.write(f"Szam: {i}\n")