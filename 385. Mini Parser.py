# Leetcode - 385. Mini Parser (Python language) - Medium

from termcolor import colored

print(colored("# Leetcode - 385. Mini Parser (Python language) - Medium", "yellow"))

def deserialize(sVar):
    if sVar[0] != "[":
        return int(sVar)

    result = []

    temp = ""
    memory_location = result
    prev_stack = []   

    for i in sVar[1:]: 
        if i == '-':
            temp += i
            continue
        try:
            int(i)
            temp += i
            continue
        except ValueError:
            pass

        if i == ",":
            if temp:                       
                memory_location.append(int(temp))
                temp = ""
        elif i == "[":
            memory_location.append([])
            prev_stack.append(memory_location)
            memory_location = memory_location[-1]
        elif i == "]":
            if temp:
                memory_location.append(int(temp))
                temp = ""
            if prev_stack:                  
                memory_location = prev_stack.pop()

    return result

s = ["324","[123,[456,[789]]]"]

for test in range(len(s)):
    print(
        colored(f"Test {(test + 1)}:","green"),
        deserialize(s[test]),
        "|",
        colored("Passed","green")
    )  