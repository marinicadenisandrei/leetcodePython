from itertools import permutations

case = 2

if case == 1:
    s = "barfoothefoobarman"
    words = ["foo","bar"]

elif case == 2:
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]

elif case == 3:
    s = "barfoofoobarthefoobarman" 
    words = ["bar","foo","the"]

lista = []
def permute(data, i, length):
    word = ""
    if i == length:
        for i in data:
            word += i
        lista.append(word)
        word = ""
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

def generate_permutations(data):
  permute(list(data), 0, len(data))

generate_permutations(words)

final = []

for i in lista:
    if i in s:
        final.append(s.find(i))

print(sorted(final))