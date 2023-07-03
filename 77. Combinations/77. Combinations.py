# Leetcode - 77. Combinations (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 77. Combinations (Python language) - Medium","yellow"))

nTest = [4, 1]
kTest = [2, 1]

for test in range(len(nTest)):

    n = nTest[test]
    k = kTest[test]

    numbers = [i for i in range(1,n+1)]

    output = [[]]
    if k < 0:
        output[-1] = "K < 0"
    elif k == 1:
        output[-1] = numbers

    elif k == 2:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    temp = [numbers[i], numbers[j]]
                    temp.sort()
                    if temp not in output[0]:
                        output[0].append(temp)

    else:
        output.append([])
        for i in range(k-2):
            output.append([])
            for j in numbers:
                for k in output[i]:
                    temp = k.copy()
                    temp.append(j)
                    temp.sort()
                    if temp not in output[len(output)-1]:
                        output[len(output)-1].append(temp)

    testNumber = test + 1

    print(colored(f"Test {testNumber}:","green"),output[-1],"|",colored("Passed","green"))


