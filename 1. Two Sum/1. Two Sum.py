nums = [[2,7,11,15],[3,2,4],[3,3]]
target = [9,6,6]
final = []

for lists,targets in zip(nums,target):
    for i in range(len(lists)):
        for j in range(1,len(lists)):
            if lists[i] + lists[j] == targets and i != j:
                final.append(i)
                final.append(j)
    print(list(set(final)))
    final = []

