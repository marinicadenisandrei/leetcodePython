# Leetcode - 99. Recover Binary Search Tree (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 99. Recover Binary Search Tree (Python language) - Medium", "yellow"))

def createFinalOutput(depth_var, list_var):
    output_var = []
    
    for i in range(depth):
        output_var.append([])
        for j in range(len(list_var)):
            output_var[i].append(list_var[j][i])
    
    return output_var

def returnDepth(length_list):
    n = 0
    power_var = 0
    
    while power_var < length_list:
        power_var = pow(2,n)
        n += 1
    
    return power_var
    
rootTest = [[1,3,0,0,2], [3,1,4,0,0,2]]

for test in range(len(rootTest)):
    root = rootTest[test]
    removeReminder = returnDepth(len(root))-len(root)

    for i in range(removeReminder):
        root.append(0)

    flag = True

    while flag:
        flag = False
        
        depth = int(len(root) / 2)
        state = depth

        counter = 1

        output = []
        signs = []
        add = 0

        flag = False

        for i in range(depth - 1):
            output.append([])
            if i > 0:
                signs.append([])
            for j in range(1,depth+1):
                if add == state:
                    counter += 1
                    add = 0
                add += 1
                
                if i > 0:
                    signs[i-1].append(sign_var)
                    
                    if add == state and flag == False:
                        flag = True
                    elif add == state and flag == True:
                        flag = False
                    
                    if flag == False:
                        sign_var = ">"
                    if flag == True:
                        sign_var = "<"
                    
                output[i].append(root[counter - 1])
            
            flag = False
            sign_var = ">"
            counter += 1
            add = 0
            state = int(state/2)

        new_output = createFinalOutput(depth, output)
        new_sign = createFinalOutput(depth, signs)

        for i,j in zip(new_output, new_sign):
            for k in range(0,len(i)):
                for l in range(k + 1,len(i)):
                    if j[k] == ">" and i[k] != 0 and i[l] != 0:
                        if i[k] < i[l]:
                            index1 = root.index(i[k])
                            index2 = root.index(i[l])
                            root[index1],  root[index2] = root[index2],  root[index1]
                            flag = True
                            break
                            
                    elif j[k] == "<" and i[k] != 0 and i[l] != 0:
                        if i[k] > i[l]:
                            index1 = root.index(i[k])
                            index2 = root.index(i[l])
                            root[index1],  root[index2] = root[index2],  root[index1]
                            flag = True
                            break
                
                if flag == True:
                    break
            
            if flag == True:
                break

    root = root[:len(root) - depth + 1]
    testNumber = test + 1
    
    print(colored(f"Test {testNumber}:", "green"), root, "|", colored("Passed", "green"))