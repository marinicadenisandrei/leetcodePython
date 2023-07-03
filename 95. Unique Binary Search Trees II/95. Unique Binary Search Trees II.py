# Leetcode - 95. Unique Binary Search Trees II (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 95. Unique Binary Search Trees II (Python language) - Medium", "yellow"))

nTest = [3, 1]

for test in range(len(nTest)):
    n = nTest[test]

    n = [_ for _ in range(1, n + 1)]

    output = []

    if len(n) == 1:
        output.append(n)

    else:
        for i in n:
            left = n[:i - 1].copy()
            right = n[i:].copy()

            if len(left) == 1 and len(right) == 1 and left[0] != 0 and right[0] != 0:
                left.insert(0, i)
                left.extend(right.copy())

                output.append(left.copy())

                left = []
                right = []

            else:
                if len(left) == 0:
                    left.append(0)
                
                if len(right) == 0:
                    right.append(0)

                if len(left) > 1:
                    temp = [[]]
                    temp[0].append(left[0])
                    temp[0].append(0)
                    temp[0].extend(left[1:])

                    temp.append([])
                    
                    for j in range(1,len(left)):
                        number = left[j]
                        left.remove(number)
                        left.sort()
                        left.insert(0, number)
                        temp.append(left)

                    left = temp

                elif len(left) == 1 and left[0] == 0:
                    left = [left]

                if len(right) > 1:
                    temp = [[]]
                    temp[0].append(right[0])
                    temp[0].append(0)
                    temp[0].extend(right[1:])

                    temp.append([])
                
                    for j in range(1,len(right)):
                        number = right[j]
                        right.remove(number)
                        right.sort()
                        right.insert(0, number)
                        temp.append(right.copy())

                    right = temp
                
                elif len(right) == 1 and right[0] == 0:
                    right = [right]
                
                formatList = []

                if len(left) == 1 and left[0][0] == 0:
                    try:
                        for k in right:
                            if len(k) > 0:
                                formatList.append(i)
                                formatList.extend(left[0])
                                formatList.extend(k)

                                output.append(formatList.copy())
                                formatList = []   
                    except TypeError:
                        pass

                else:
                    for k in left:
                        if len(k) > 0:
                            formatList.append(i)
                            formatList.append(k[0])
                            formatList.extend(right[0].copy())
                            formatList.extend(k[1:].copy())

                            output.append(formatList)
                            formatList = []

    testNumber = test + 1
    print(colored(f"Test {testNumber}:", "green"), output, "|", colored("Passed", "green"))

    

    
