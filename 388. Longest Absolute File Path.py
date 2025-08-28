# Leetcode - 388. Longest Absolute File Path (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 388. Longest Absolute File Path (Python language) - Medium","yellow"))

def lengthLongestPath(inputVar):
    result = 0
    tempCount = 0
    lastLen = 0
    level = -1

    for i in inputVar.split("\n"):
        if level < i.count("\t"):
            level += 1
            tempCount += len(i)
            lastLen = len(i)
            
        else:
            tempCount -= lastLen
            tempCount += len(i)
            
            if result < tempCount - 1:
                result = tempCount - 1

    if result < tempCount - 1:
        result = tempCount - 1
    
    return result
        
input = ["dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext","dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext","a"]

for test in range(len(input)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        lengthLongestPath(input[test]),
        "|",
        colored("Passed","green")
    )
    