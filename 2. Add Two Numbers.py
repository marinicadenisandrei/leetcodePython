from termcolor import colored

l1 = [[2,4,3],[0],[9,9,9,9,9,9,9]]
l2 = [[5,6,4],[0],[9,9,9,9]]

output = []

counter_test = 1

for x,y in zip(l1,l2):
    if len(x) != len(y):
        if len(x) > len(y):
            add_counter = len(x) - len(y)
            for _ in range(add_counter): y.append(0)
        else:
            add_counter = len(x) - len(y)
            for _ in range(add_counter): x.append(0)
        
    
        carry = 0
        
        for i,j in zip(x,y):
            if i+j+carry > 10:
                output.append(i+j+carry-10)
                carry = 1
            if i+j+carry == 10:
                output.append(0)
                carry = 1
        
        if carry == 1:
            output.append(1)
            
    elif len(x) == 1 and len(y) == 1:
        output.append(x[0] + y[0])
        
    else:
        x = int("".join(str(i) for i in x))
        y = int("".join(str(i) for i in y))

        output.extend(str(x+y))
        output = [int(i) for i in reversed(output)]
    
    text = colored(f"Test {counter_test}: ", "green")
    state = colored("Passed", "green")
    
    print(f"{text}{output} | {state}")
    
    output = []
    carry = 0 
    counter_test += 1
    
    


        