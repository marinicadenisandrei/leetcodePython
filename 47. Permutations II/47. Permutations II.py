import random
import time
import itertools

nums = [[1,2,3],[0,1],[1]]
final = []

counter_test = 1

print("First example\n")
for test in nums:
    factorial = 1
    for i in range(1,len(test)+1):
        factorial *= i
# FIRST EXAMPLE
    while len(final) < factorial:
        shuffled_nums = test.copy()
        random.shuffle(shuffled_nums)

        if shuffled_nums not in final:
            final.append(shuffled_nums)

    print(f"Test {counter_test}: {final}")
    final = []
    counter_test += 1 
    

# SECOND EXAMPLE
nums = [[1,2,3],[0,1],[1]]
final = []
print("\n\nSecond example\n")
test_count = 1

for test in nums:

    copie = test.copy()

    factorial = 1
    for i in range(1,len(test)+1):
        factorial *= i

    j = 1
    counter = 0
    counter_big = 1

    for i in range(len(test)):
        while(counter < factorial/len(test)):
            if j < len(test)-1:
                test[j], test[j+1] = test[j+1], test[j]
            

            if j == len(test)-1:
                test[-1], test[1] = test[1], test[-1]
                j = 0
            
            j += 1
            counter += 1
            final.append(test.copy())

        j = 1
        counter = 0

        test = []
        test.extend(copie)
        try:
            test[0],test[counter_big] = test[counter_big], test[0]
            final.append(test)
            counter_big += 1
            
        except IndexError:
            break

    final = [str(i) for i in final]
    final = list(dict.fromkeys(final))
    
    print(f"Test {test_count}: {final}")
    
    final = []
    test_count += 1