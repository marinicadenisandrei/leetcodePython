from termcolor import colored

testNums = [[2,3,1,1,4], [3,2,1,0,4]]
state = colored("Passed", "green")

for test,counterTest in zip(testNums,range(1,len(testNums)+1)):
    nums = test
    final = len(nums)
    indexStep = 0
    stop = len(nums)
    factor = 0

    options = []
    options.append(indexStep)
    removeIndex = []
    triggerIndex = 0
    flag = False
    flagSystem = False
    flagFinder = False

    while(stop > 1 and flagSystem == False):
        if nums[indexStep] != 0:
            if indexStep == triggerIndex:
                indexStep -= factor
            stop -= nums[indexStep]
            indexStep += nums[indexStep]
            options.append(indexStep)
        else:
            flag = any(nums[op] > 1 for op in options)
            if flag == True:
                for i in range(len(options)-1,-1,-1):
                    if nums[options[i]] <= 1:
                        removeIndex.append(i)
                    else:
                        options = [options[i] for i in range(len(options)) if i not in removeIndex]
                        removeIndex = []
                        triggerIndex = options.index(options[-1])
                        nums[triggerIndex] -= 1
                        stop = len(nums)
                        break   
            else:
                flagSystem = True
        
        if stop == 1:
            flagFinder = True
            text = colored(f"Test {counterTest}: ")
            print(f"Test {counterTest}: {True} | {state}")
            break

    if flagFinder == False:
        print(f"Test {counterTest}: {False} | {state}")









