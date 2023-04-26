nums = [-1,2,1,-4]
target = 1
lista = []
sums = []

dictionar = {}

for i in nums:
    for j in nums:
        for k in nums:
            if i+j+k not in dictionar.values():
                dictionar[f"{i}+{j}+{k}="] = i+j+k
                sums.append(i+j+k)                  

def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))

last = [f"{key}{value}" for (key,value) in dictionar.items() if value == takeClosest(target,sums)]

print(f"The sum that is closest to the target is {last[0].split('=')[1]}. {last[0]}")