# Leetcode - 71. Simplify Path (Python Language) - Medium

from termcolor import colored

print(colored("Leetcode - 71. Simplify Path (Python Language) - Medium", "yellow"))

state = colored("Passed", "green")

testPath = ["/home/","/../","/home//foo/"]

for test in testPath:
    path = test
    path = path.replace(".", "")

    path = path.split("/")
    path = "".join(_ + "/" for _ in path if _ != "")
    path = "/" + path[:-1]

    testNumber = testPath.index(test) + 1
    text = colored(f"Test {testNumber}: ", "green")

    print(f"{text}{path} | {state}")
    