head = [1,2,3,4]

if len(head) > 1:
    for i,j in zip(range(0,len(head),2),range(1,len(head),2)):
        head[i], head[j] = head[j], head[i]
    print(head)
elif len(head) < 2:
   print(head)


