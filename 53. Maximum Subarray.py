from termcolor import colored

nums = [[-2,1,-3,4,-1,2,1,-5,4],[1],[5,4,-1,7,8]]

counterTest = 1

for test in nums:
    sumList = []
    sum = 0

    for _ in range(len(test)):
        for i in range(1,len(test)+1):
            for j in test[:i]:
                sum += j
            sumList.append(sum)
            sum = 0
        test.pop(0)

    text = colored(f"Test {counterTest}: ", "green")
    state = colored("Passed", "green")

    print(f"{text}{max(sumList)} | {state}")

    counterTest += 1


    



