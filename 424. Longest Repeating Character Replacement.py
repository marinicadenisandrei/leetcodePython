# Leetcode - 424. Longest Repeating Character Replacement (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 424. Longest Repeating Character Replacement (Python language) - Medium", "yellow"))

def characterReplacement(sVar, kVar):
    candidates = "".join(set(s))
    result = 0

    for i in candidates:
        indexCandidates = [j for j in range(len(sVar)) if sVar[j] == i]
        indexCandidates.append(0)
        indexCandidates.sort()
        
        for j in indexCandidates:
            check_sVar = sVar[j:]
            temp_k = kVar
            temp_result = 0
            
            for k in check_sVar:
                if k == i:
                    temp_result += 1
                elif k != i and temp_k > 0:
                    temp_result += 1
                    temp_k -= 1
                else:
                    break
            
            if result < temp_result:
                result = temp_result

    return result


s = ["ABAB","AABABBA"]
k = [2,1]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        characterReplacement(s[test], k[test]),
        "|",
        colored("Passed","green")
    )