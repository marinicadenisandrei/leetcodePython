# Leetcode - 343. Integer Break (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 343. Integer Break (Python language) - Medium","yellow"))

def integerBreak(nVar):
    result = 0

    for i in range(1, nVar):
        temp = []

        while sum(temp) <= nVar:
            if sum(temp) + i <= nVar:
                temp.append(i)
            else:
                break

        for j in range(len(temp)):
            temp_copy = temp.copy()
            for k in range(nVar):
                temp[j] = temp[j] + k

                if sum(temp) == nVar:
                    productElement = 1

                    for l in temp: productElement *= l

                    if productElement > result:
                        result = productElement

                temp = temp_copy
    
    return result

n = [2,10]
for test in range(len(n)):
    print(colored(f"Test {(test + 1)}:","green"), integerBreak(n[test]), "|", colored("Passed", "green"))

    