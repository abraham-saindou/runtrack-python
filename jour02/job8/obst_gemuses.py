def fruits_legumes(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("Artichaut, aubergine, navet")

fruits_legumes("fruits", "hiver")
fruits_legumes("legumes", "hiver")
fruits_legumes("fruits", "ete")
fruits_legumes("legumes", "hiver")