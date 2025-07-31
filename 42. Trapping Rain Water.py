# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

big = []

for i in range(len(height)):
    big.append([])
    for j in range(height[i]):
        big[i].append("x")
    
    if len(big[i]) != max(height):
        for k in range(max(height) - len(big[i])):
            big[i].append("0")



test = []
counter = 0


for j in range(max(height)):
    for i in range(len(big)):
        test.append(big[i][j])

    if test[0] == "0":
        for i in range(len(test)):
            if test[i] == "x":
                test = test[i:]
                break
    
    if test[-1] == "0":
        for i in reversed(range(len(test))):
            if test[i] == "x":
                test = test[:i+1]
                break
    
    for i in test:
        if i == "0":
            counter += 1
    
    test = []

print(counter)

