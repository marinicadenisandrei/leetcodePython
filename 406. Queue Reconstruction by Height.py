# Leetcode - 406. Queue Reconstruction by Height (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 406. Queue Reconstruction by Height (Python language) - Medium","yellow"))

def reconstructQueue(peopleVar):
    peopleVar = sorted(peopleVar, key=lambda x: (-x[0], x[1]))
    
    result = []
    for person in peopleVar:
        result.insert(person[1], person)
    
    return result

people = [[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]],[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]]

for test in range(len(people)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        reconstructQueue(people[test]),
        "|",
        colored("Passed","green")
    )