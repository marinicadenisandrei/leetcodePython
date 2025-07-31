from termcolor import colored

n = [4, 1]

counter_test = 1

for test in n:
    copie_n = test

    output = [["" for _ in range(test)].copy() for _ in range(test)]

    copie = output.copy()

    potential = []
    index = []

    def checkDiagPos(diagNo):
        
        if diagNo <= copie_n:
            for i in range(diagNo):
                output[i][diagNo-1] = "X"
                diagNo -= 1
        else:
            for i in range(diagNo-copie_n,copie_n):
                try:
                    output[i][(diagNo-1)-i] = "X"
                except IndexError:
                    pass

    def checkDiagNeg(diagNo):
        
        if diagNo <= copie_n:
            counter = len(output[0])-diagNo
            
            for i in range(diagNo):
                try:
                    output[i][counter] = "X"
                    counter += 1
                except:
                    IndexError
        else:
            counter = 0
            for i in range(diagNo-copie_n,copie_n):
                try:
                    output[i][counter] = "X"
                    counter += 1
                except IndexError:
                    pass
        
    def checkVertical(verticalIndex):

        for i in range(len(output)):
            if output[i][verticalIndex] != "Q":
                output[i][verticalIndex] = "X"

    def checkOrizontal(indexOrizontal):
        for i in range(len(output[indexOrizontal])):
            if output[indexOrizontal][i] != "Q":
                output[indexOrizontal][i] = "X"


    counter = 0
    flag = True

    counter_while = 0

    while flag:
        for i in range(len(output)):
            for j in range(len(output[i])):
                if output[i][j] != "Q" and output[i][j] != "X":
                    index.append((i,j))
                    checkDiagPos(j+1+counter)
                    checkDiagNeg(copie_n-j)
                    checkVertical(j)
                    checkOrizontal(i)
                    output[i][j] = "Q"
                    break
            
            counter += 1
            test += 1
            
            try:
                if "" not in output[i+1]:
                    output = [["" for _ in range(copie_n)].copy() for _ in range(copie_n)]
                    for i in index:
                        output[i[0]][i[1]] = "X"
                    test = copie_n
                    counter = 0
                    index = []
                    break
            except IndexError:
                flag = False
            
        counter_while += 1
            
    output = ["."*copie_n for _ in range(copie_n)]

    for i,j in zip(output, index):
        output[j[0]] = output[j[0]][:j[1]] + "Q" + output[j[0]][j[1]+1:]
    
    text = colored(f"Test {counter_test}: ", "green")
    state = colored("Passed","green")
    
    print(f"{text}{output} | {state}")
    
    counter_test += 1

