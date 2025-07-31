lists = [[1,4,5], [1,3,4], [2,6]]
final = []

for i in lists:
    for j in i:
        final.append(j)

final.sort()
print(final)
