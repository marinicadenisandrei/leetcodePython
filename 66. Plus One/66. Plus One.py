# Leetcode - 66. Plus One (Python Language)

from termcolor import colored

problemName = colored("Leetcode - 66. Plus One (Python language)", "yellow")
print(problemName)

state = colored("Passed", "green")

digits = [[1,2,3], [4,3,2,1], [9]]

for test in digits:

    copieTest = test.copy()

    test = str(test)
    newDigits = ""

    for i in test:
        if i.isdigit():
            newDigits += i

    newDigits = int(newDigits)
    newDigits = newDigits + 1

    output = []

    for i in str(newDigits):
        output.append(int(i))

    numberTest = digits.index(copieTest) + 1
    text = colored(f"Test {numberTest}: ", "green")

    print(f"{text}{output} | {state}")

    output = []