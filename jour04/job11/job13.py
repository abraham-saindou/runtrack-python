def tri():
    listitem = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    for i in listitem:
        x = listitem[i]
        if x == x:
            listitem.pop(x)
        print(listitem)
        listitem[i] + 1
tri()