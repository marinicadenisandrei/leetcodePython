# Leetcode - 301. Remove Invalid Parentheses (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 301. Remove Invalid Parentheses (Python language) -","yellow"), colored("Hard","red"))

def removeInvalidParentheses(sVar):
    candidates = []
    result = []
    sVar = "".join([char for char in sVar if char in '()'])
    sorted_s = "".join(sorted(sVar))
    sorted_s = "".join([char for char in sorted_s if char in '()'])
    
    for i in range(int(len(sorted_s)/2)):
        if sorted_s[i] == "(" and sorted_s[-i] != ")":
            sorted_s = sorted_s[:i] + sorted_s[:-i-1]
    
    depth = int(len(sorted_s)/2) - 1
    candidates.append("()" * (depth + 1))

    for i in range(depth):
        temp = ""

        for j in range(depth):
            if j == i:
                temp += "(())"
            else:
                temp += "()"
        
        candidates.append(temp)
    
    for i in candidates:
        for j in range(len(sVar)):
            if i in sVar[:j] + sVar[j+1:]:
                result.append(i)
                break
    
    return result
  
s = ["()())()","(a)())()",")("]

for test in range(len(s)):
    print(colored(f"Test {(test + 1)}:","green"), removeInvalidParentheses(s[test]), "|", colored("Passed","green"))