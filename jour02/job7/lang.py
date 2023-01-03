def parole(langage):
    match langage:
        case "javascript":
            print("Tu es un developpeur web")
        case "python":
            print("Tu es un developpeur IA")
        case "java":
            print("Tu es un developpeur logiciel")
        case "reactjs":
            print("Tu es un developpeur mobile")
        case _:
            print("Un jour, je serai le meilleur developpeur...")

parole("python")
parole("java")
parole("tout")