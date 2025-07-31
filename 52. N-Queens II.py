from termcolor import colored

n = [4, 1]

counter_test = 1

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
            output[i][counter] = "X"
            counter += 1
           
    else:
        counter = 0
        for i in range(diagNo-copie_n,copie_n):
            output[i][counter] = "X"
            counter += 1
    
def checkVertical(verticalIndex):

    for i in range(len(output)):
        if output[i][verticalIndex] != "Q":
            output[i][verticalIndex] = "X"

def checkOrizontal(indexOrizontal):
    for i in range(len(output[indexOrizontal])):
        if output[indexOrizontal][i] != "Q":
            output[indexOrizontal][i] = "X"

for test in n:
    copie_n = test

    output = [["" for _ in range(test)].copy() for _ in range(test)]

    copie = output.copy()

    potential = []
    index = []

    counter = 0
    flag = True

    counter_while = 0

    while flag:
        for i in range(len(output)):
            for j in range(len(output[i])):
                if output[i][j] != "Q" and output[i][j] != "X":
                    index.append((i,j))
                    checkDiagPos(j+1+counter)
                    checkDiagNeg(copie_n-j+counter)
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
                break
        
            
    counter_while += 1
    
    output = ["."*copie_n for _ in range(copie_n)]

    for i,j in zip(output, index):
        output[j[0]] = output[j[0]][:j[1]] + "Q" + output[j[0]][j[1]+1:]
    
    lista2 = [i[::-1] for i in output]

    counter_variants = 1
    flag_equal = False

    for i,j in zip(output,lista2):
        if i == j:
            flag_equal = True

    if flag_equal == False: counter_variants += 1
    
    text = colored(f"Test {counter_test}: ", "green")
    state = colored("Passed","green")
    
    print(f"{text}{counter_variants} | {state}")
    
    counter_test += 1




