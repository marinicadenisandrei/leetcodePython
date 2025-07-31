# Leetcode - 97. Interleaving String (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 97. Interleaving String (Python language) - Medium", "yellow"))

s1Test = ["aabcc", "aabcc" , ""]
s2Test = ["dbbca", "dbbca", ""]
s3Test = ["aadbbcbcac", "aadbbbaccc", ""]

for test in range(len(s1Test)):
    s1 = s1Test[test]
    s2 = s2Test[test]
    s3 = s3Test[test]

    chooseList = [s1, s2]
    flagChoose = True

    counter = 0

    while len(s3) > 0:
        choose_var = 0

        for i in range(len(chooseList)):
            flagChoose = False
            try:
                if s3[0] == chooseList[i][0]:
                    choose_var = i
                    flagChoose = True
                    break
            except IndexError:
                flagChoose = False
        
        if flagChoose == False:
            break
            

        for i,j in zip(s3, chooseList[choose_var]):
            if i == j:
                s3 = s3[1:]
                chooseList[choose_var] = chooseList[choose_var][1:]

        counter += 1

    flag = False

    if len(s3) == 0:
        flag = True
    
    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"), flag, "|", colored("Passed", "green"))


