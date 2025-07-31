head = [1,2,3,4,5]
k = 2


for i, j in zip(range(0,len(head),k), range(k-1,len(head),k)):
    head[i], head[j] = head[j], head[i]

print(head)


    