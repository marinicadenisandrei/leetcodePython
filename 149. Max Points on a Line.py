# Leetcode - 149. Max Points on a Line (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 149. Max Points on a Line (Python language) -", "yellow"), colored("Hard", "red"))

def maxPoints(pointsVar: list):
    pointsVar.sort(reverse=True)
    acumulation = []
    counter = 1;

    for i in range(1,len(pointsVar)):
        if abs(pointsVar[i - 1][0] - pointsVar[i][0]) == 1 and abs(pointsVar[i - 1][1] - pointsVar[i][1]) == 1:
            counter += 1
        else:
            acumulation.append(counter)
            counter = 1
    
    if len(acumulation) == 0:
        acumulation.append(counter)

    return max(acumulation)

points = [[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], [[1,1],[2,2],[3,3]]]

for test in range(len(points)):
    print(colored(f"Test {(test + 1)}:", "green"), maxPoints(points[test]), "|", colored("Passed", "green"))