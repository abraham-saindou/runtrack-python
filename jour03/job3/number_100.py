def number():
    i = 0
    while i < 100:
        i = i + 1
        if i == 26 or i == 37 or i == 88:
            continue
        print(i)

number()