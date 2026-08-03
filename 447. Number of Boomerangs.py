# Leetcode - 447. Number of Boomerangs (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 447. Number of Boomerangs (Python language) - Medium","yellow"))

def numberOfBoomerangs(pointsVar):
    result = 0

    for i in pointsVar:                        
        distante = {}                       

        for j in pointsVar:                    
            d = (i[0]-j[0])**2 + (i[1]-j[1])**2
            distante[d] = distante.get(d, 0) + 1

        for n in distante.values():         
            result += n * (n - 1)

    return result

points = [[[0,0],[1,0],[2,0]],[[1,1],[2,2],[3,3]],[[1,1]]]

for test in range(len(points)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        numberOfBoomerangs(points[test]),
        "|",
        colored("Passed", "green")
    )