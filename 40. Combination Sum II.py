# Leetcode - 40. Combination Sum II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 40. Combination Sum II (Python language) - Medium", "yellow"))

candidatesTest = [[10,1,2,7,6,1,5], [2,5,2,1,2]]
targetTest = [8, 5]

for test in range(len(candidatesTest)):
    candidates = candidatesTest[test]
    target = targetTest[test]

    output = [[[i] for i in candidates]]
    result = []

    for i in candidates:
        if i == target:
            result.append([i])

    index_location = 0
    flag = True

    while flag:
        flag = False
        output.append([])

        for i in candidates:
            for j in output[index_location]:
                temp = j.copy()
                temp.append(i)

                if sum(temp) == target:
                    temp.sort()
                    if temp not in result:
                        result.append(temp.copy())
                
                if sum(temp) < target:
                    flag = True

                output[index_location + 1].append(temp.copy())

                temp.clear()

        index_location += 1

        if index_location == 2:
            break

    
    testNumber = test + 1

    print(colored(f"Test {testNumber}:", "green"), result, "|", colored("Passed", "green"))


        