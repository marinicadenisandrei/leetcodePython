word1 = "horse"
word2 = "ros"

charaterFound = []

characterFound = [word1.index(char) for char in word2]

# eliminate elements which are not in ascending order

word1 = [word1[i] if i in characterFound else "" for i in range(len(word1))]

print(word1)

