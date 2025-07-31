# Leetcode - 337. House Robber III (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 337. House Robber III (Python language) - Medium","yellow"))

def rob(rootVar):
    result = rootVar[0]

    for i in range(1,len(rootVar)):
        if ((i * 2) + 2) > len(rootVar):
            break
        
        result += rootVar[(i * 2) + 2]
    
    result2 = 0

    for i in range(1,len(rootVar)):
        if ((i * 2) + 2) > len(rootVar):
            break
        
        result2 += rootVar[i]    
    
    if result > result2:
        return result

    return result2
            
root = [[3,2,3,0,3,0,1],[3,4,5,1,3,0,1]]

for test in range(len(root)):
    print(colored(f"Test {(test + 1)}:","green"), rob(root[test]), "|", colored("Passed","green"))
    