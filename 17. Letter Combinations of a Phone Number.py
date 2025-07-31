digits = "23"

dictionar = {
    "2": ["a","b","c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

lista = []

for i in digits:
    lista.extend([dictionar[i]])

final = []
    
if len(lista) >=2:
    for i in lista[0]:
        for j in lista[1:]:
            for k in j:
                final.append(i+k)

    print(final)

elif len(lista) == 1:
    print(lista[0])

else:
    print([])