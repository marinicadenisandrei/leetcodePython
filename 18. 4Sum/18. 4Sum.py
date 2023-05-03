nums = [1,0,-1,0,-2,2]

unique=[i for i in nums if nums.count(i)==1]
        
seen = set()
dupes = [x for x in nums if x in seen or seen.add(x)]  

target = 0
lista = []

for i in nums:
    for j in nums:
        for k in nums:
            for l in nums:
                if i+j+k+l == target:
                    lista.append([i,j,k,l])


for i in lista:
    i.sort()

dict_tuple = {tuple(item): index for index, item in enumerate(lista)}
final = [list(itm) for itm in dict_tuple.keys()]

for i in unique:
    for j in final:
        if j.count(i) > 1 or j.count(j[0]) == 4:
            final.remove(j)


print(final)




