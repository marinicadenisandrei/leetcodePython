import random
import time
import itertools

nums = [1,2,3]
# nums = [1,2,3,4]
final = []

# FIRST EXAMPLE
# while len(final) < 24:
#     shuffled_nums = nums.copy()
#     random.shuffle(shuffled_nums)

#     if shuffled_nums not in final:
#         final.append(shuffled_nums)

# print(final)  



# SECOND EXAMPLE

copie = nums.copy()

factorial = 1
for i in range(1,len(nums)+1):
    factorial *= i

j = 1
counter = 0
counter_big = 1

for i in range(len(nums)):
    while(counter < factorial/len(nums)):
        if j < len(nums)-1:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        

        if j == len(nums)-1:
            nums[-1], nums[1] = nums[1], nums[-1]
            j = 0
        
        j += 1
        counter += 1
        final.append(nums.copy())

    j = 1
    counter = 0

    nums = []
    nums.extend(copie)
    try:
        nums[0],nums[counter_big] = nums[counter_big], nums[0]
        final.append(nums)
        counter_big += 1
        
    except IndexError:
        break

final = [str(i) for i in final]
final = list(dict.fromkeys(final))
 
for i in enumerate(final):
    print(i)
    # input()





