k = 96

for i in range(1, 30):
    for j in range(1, i + 1):
        k += 1
        a = chr(k)
        print(a, end=" ")
        for l in range(0, 10):
            if k == 122:
                k = 96
    print()