import string

def listAlphabet():
    return sorted(list(string.ascii_uppercase), reverse=True)
print(listAlphabet())
