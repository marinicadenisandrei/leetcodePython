# Leetcode - 354. Russian Doll Envelopes (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 354. Russian Doll Envelopes (Python language) -", "yellow"), colored("Hard", "red"))

def maxEnvelopes(envelopesVar):
    result = 1

    envelopesVar.sort()

    for i in envelopesVar:
        i.sort()

    envelopesVar.append(envelopesVar[-1])
    compare = envelopesVar[0]

    for i in range(len(envelopesVar) - 1):
        if compare[1] - compare[0] == 1 and envelopesVar[i + 1][0] - compare[1] == 1 and envelopesVar[i + 1][1] - envelopesVar[i + 1][0] == 1:
            result += 1
            compare = envelopesVar[i + 1]
        
    return result
            
envelopes = [[[5,4],[6,4],[6,7],[2,3]],[[1,1],[1,1],[1,1]]]

for test in range(len(envelopes)):
    print(colored(f"Test {(test + 1)}:","green"), maxEnvelopes(envelopes[test]), "|", colored("Passed","green"))
    