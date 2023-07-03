from termcolor import colored

matrix = [[[1,2,3],[4,5,6],[7,8,9]],[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]

counter_test = 1

for tests in matrix:
    l = [[0].copy()*len(tests) for _ in range(len(tests))]

    for i in range(len(tests)):
        for j in range(1,len(tests)+1):
            l[i][-j] = tests[j-1][i]
    
    text = colored(f"Test {counter_test}: ","green")
    print(f"{text} {l}")

    l = []
    counter_test += 1


