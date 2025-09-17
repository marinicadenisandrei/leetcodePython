# Leetcode - 395. Longest Substring with At Least K Repeating Characters (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 395. Longest Substring with At Least K Repeating Characters (Python language) - Medium","yellow"))

def longestSubstring(sVar, kVar):
    occ = dict()
    result = 0;

    for i in sVar:
        if i not in occ:
            occ[i] = 1
        else:
            occ[i] += 1
    
    for key, val in occ.items():
        if kVar <= val:
            result += val
    
    return result
    
s = ["aaabb","ababbc"]
k = [3,2]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        longestSubstring(s[test],k[test]),
        "|",
        colored("Passed","green")
    )
