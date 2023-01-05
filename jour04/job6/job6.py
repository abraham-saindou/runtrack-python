def change():
    list = [1, 2, 3, 4, 5]
    print(list)

    prem = list[0]
    last = list[4]
    list[0] = last
    list[4] = prem

    print(list)
change()