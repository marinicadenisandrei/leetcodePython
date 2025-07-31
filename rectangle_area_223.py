# Leetcode - 223. Rectangle Area (Python language) - Medium

from termcolor import colored
print(colored("Leetcode - 223. Rectangle Area (Python language) - Medium","yellow"))

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    total = 0
    
    overlapx = [ax1, ax2, bx1, bx2]
    overlapy = [ay1, ay2, by1, by2]
    overlapx.sort()
    overlapy.sort()
    
    rectangle1 = (abs(ax1) + abs(ax2)) * (abs(ay1) + abs(ay2))
    rectangle2 = (abs(bx1) + abs(bx2)) * (abs(by1) + abs(by2))

    overlap = overlapx[int(len(overlapx) / 2)] * overlapy[int(len(overlapy) / 2)]
    total = rectangle1 + rectangle2

    if ax1 == bx1 and ax2 == bx2 and ay1 == by1 and ay2 == by2:
        return int(total / 2)
    else:
        return total - overlap

ax1 = [-3,-2] 
ay1 = [0,-2]

ax2 = [3,2] 
ay2 = [4,2]

bx1 = [0,-2] 
by1 = [-1,-2]

bx2 = [9,2]
by2 = [2,2]

for test in range(len(ax1)):
    print(colored(f"Test {(test + 1)}:","green"), computeArea(ax1[test], ay1[test], ax2[test], ay2[test], bx1[test], by1[test], bx2[test], by2[test]), "|", colored("Passed","green"))