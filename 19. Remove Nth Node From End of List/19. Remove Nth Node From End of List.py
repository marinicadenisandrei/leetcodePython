head = [1,2,3,4,5]

if len(head) % 2 != 0:
    head.append("x")

n = 2
counter = 1

for i in range(1,len(head)+1,2):
    if counter == n:
        head.remove(head[i])
    counter +=1

if "x" in head:
    head.pop()

print(head)