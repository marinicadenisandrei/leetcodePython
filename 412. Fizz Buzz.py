# Leetcode - 412. Fizz Buzz (Python language) - Easy

from termcolor import colored

print(colored("Leetcode - 412. Fizz Buzz (Python language) -", "yellow"), colored("Easy","green"))

def fizzBuzz(nVar):
    result = []

    for i in range(1, nVar + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
             result.append("Fizz")
        elif i % 5 == 0:
             result.append("Buzz")
        else:
            result.append(str(i))

    return result

n = [3,5,15]

for test in range(len(n)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        fizzBuzz(n[test]),
        "|",
        colored("Passed","green")
    )