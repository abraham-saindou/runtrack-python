def list():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    produit = 1
    for i in range(len(L)):
        if L[i] <= 25 or L[i] >= 90:
            pass
        else:
            produit *= L[i]
    print(produit)

list()