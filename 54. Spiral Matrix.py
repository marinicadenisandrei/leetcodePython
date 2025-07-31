from termcolor import colored

matrix = [[[1,2,3],[4,5,6],[7,8,9]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]]]

output = []
counterTest = 1

for test in matrix:
    while(len(test) != 1):
        output.extend(test[0].copy())

        for i in test[1:-1]:
            output.append(i[-1])

        output.extend(test[-1][::-1].copy())

        for i in reversed(test[1:-1]):
            output.append(i[0])

        
        try:
            test.pop(0)
            test.pop(-1)
            test[0].pop(0)
            test[-1].pop(-1)
        except IndexError:
            break
    
    try:
        output.extend(test[0].copy())
    except IndexError:
        break
            
    text = colored(f"Test {counterTest}: ","green")
    state = colored("Passed", "green")

    print(f"{text}{output} | {state}")

    output = []
    counterTest += 1

