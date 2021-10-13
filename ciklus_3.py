i = 1
k = 2
l = 1
while k <= 12:
    l = k % 2
    if l == 0:
        i = i * 3
        print(str(k) + ".:",i)
    else:
        print(str(k) + ".:", i)
    k=k+1
