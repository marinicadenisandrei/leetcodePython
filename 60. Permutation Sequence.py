# Leetcode - 60. Permutation Sequence (Python language)

print("Leetcode - 60. Permutation Sequence (Python language)")

from termcolor import colored

testPer = [3,4,3]
testIndex = [3,9,1]

state = colored("Passed", "green")

def factorialLength(numberOfElements):

    depth = 1

    for i in range(1,numberOfElements+1):
        depth *= i
    
    return depth

for test in range(len(testPer)):

    n = testPer[test]
    k = testIndex[test]

    n_copy = n

    n = [i for i in range(1,n+1)]
    n_list_copy = n.copy()
    output = []

    flag = True

    indexSwitch = 1

    for i in range(n_copy):
        checkList = n.copy()
        while(flag):
            output.append(n.copy())
            if indexSwitch < n_copy-1:
                n[indexSwitch], n[indexSwitch+1] = n[indexSwitch+1], n[indexSwitch] 
                indexSwitch += 1
            else:
                n[1], n[-1] = n[-1], n[1]
                indexSwitch = 1
            
            if n == checkList:
                break
        
        try:
            temp = [n_list_copy[i+1]]
        except IndexError:
            break

        n.remove(n_list_copy[i+1])
        n.sort()
        temp.extend(n.copy())
        n = temp.copy()

        temp = []
        indexSwitch = 1
        flag = True
        


    output.sort()

    final = "".join(str(_) for _ in output[k-1])

    testNumber = test + 1
    text = colored(f"Test {testNumber}", "green")

    print(f'{text}: "{final}" | {state}')

    output = []
    checkList = []
    flag = True
    indexSwitch = 1
