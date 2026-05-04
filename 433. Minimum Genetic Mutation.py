# Leetcode - 433. Minimum Genetic Mutation (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 433. Minimum Genetic Mutation (Python language) - Medium", "yellow"))

def minMutation(startGeneVar, endGeneVar, bankGeneVar):
    mutations = [endGeneVar]

    for i in range(len(startGeneVar)):
        if startGeneVar[i] != endGeneVar[i]:
            temp = startGeneVar[:i] + endGeneVar[i] + startGeneVar[i + 1:]

            if temp in bankGeneVar:
                mutations.append(temp)
    
    mutations = list(dict.fromkeys(mutations))

    return len(mutations)

startGene = ["AACCGGTT","AACCGGTT"]
endGene = ["AACCGGTA","AAACGGTA"]
bank = [["AACCGGTA"],["AACCGGTA","AACCGCTA","AAACGGTA"]]

for test in range(len(startGene)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        minMutation(startGene[test], endGene[test], bank[test]),
        "|",
        colored("Passed", "green")
    )