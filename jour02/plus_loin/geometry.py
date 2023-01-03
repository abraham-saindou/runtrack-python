import math
def triangle(ab, ac, bc):
    if ab == ac == bc:
        print("Le triangle sera équilatéral")
    elif ab == bc or bc == ac or ac == ab:
        print("Le triangle sera isocèle")
    # On utilise ci-dessous le théorème de Pythagore pour savoir si le triangle est rectangle
    # et la fonction pow() de la librairie math
    elif pow(bc, 2) == pow(ab, 2) + pow(ac, 2):
        print("Le triangle sera rectangle")
    elif pow(bc, 2) == pow(ab, 2) + pow(ac, 2) and pow(ab, 2) == pow(ac, 2):
        print("Le triangle sera rectangle et isocèle")
    else:
        print("Le triangle sera quelcconque")

triangle(5, 5, 5)
triangle(5, 7, 5)
triangle(8, 6, 10)
triangle(3, 4, 7)