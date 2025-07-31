# Leetcode - 341. Flatten Nested List Iterator (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 341. Flatten Nested List Iterator (Python language) - Medium", "yellow"))

def NestedIterator(nestedListVar):
    result = []

    for item in nestedListVar:
        if isinstance(item, list):
            result.extend(NestedIterator(item))
        else:
            result.append(item)
    return result
    
nestedList = [[[1,1],2,[1,1]],[1,[4,[6]]]]

for test in range(len(nestedList)):
    print(colored(f"Test {(test + 1)}:","green"), NestedIterator(nestedList[test]), "|", colored("Passed","green"))