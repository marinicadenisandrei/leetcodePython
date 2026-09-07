# Leetcode - 452. Minimum Number of Arrows to Burst Balloons (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 452. Minimum Number of Arrows to Burst Balloons (Python language) - Medium", "yellow"))

def findMinArrowShots(pointsVar):
    pointsVar.sort(key=lambda x: x[1])

    arrows = 1
    arrow_position = pointsVar[0][1]

    for start, end in pointsVar[1:]:
        if start > arrow_position:
            arrows += 1
            arrow_position = end

    return arrows


points = [[[10,16],[2,8],[1,6],[7,12]],[[1,2],[3,4],[5,6],[7,8]],[[1,2],[2,3],[3,4],[4,5]]]

for test in range(len(points)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        findMinArrowShots(points[test]),
        "|",
        colored("Passed", "green")
    )