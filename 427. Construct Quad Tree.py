# Leetcode - 427. Construct Quad Tree (Python language) - Medium

from termcolor import colored

print(colored("Leetcode - 427. Construct Quad Tree (Python language) - Medium", "yellow"))

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def divideInFour(gridVar):
    result = []

    half = len(gridVar) // 2
    end = len(gridVar)

    fourLimits = [
        [0, half, 0, half],
        [0, half, half, end],
        [half, end, 0, half],
        [half, end, half, end]
    ]

    for i in fourLimits:
        temp = []
        for j in gridVar[i[0]:i[1]]:
            temp.append(j[i[2]:i[3]])
        result.append(temp)

    return result


def constructQuadTree(gridVar):
    first = gridVar[0][0]
    same = True

    for row in gridVar:
        for cell in row:
            if cell != first:
                same = False
                break
        if not same:
            break

    if same:
        return Node(bool(first), True)

    parts = divideInFour(gridVar)

    topLeft = constructQuadTree(parts[0])
    topRight = constructQuadTree(parts[1])
    bottomLeft = constructQuadTree(parts[2])
    bottomRight = constructQuadTree(parts[3])

    return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)


def serialize(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append([1 if node.val else 0, 1 if node.isLeaf else 0])

        if not node.isLeaf:
            queue.append(node.topLeft)
            queue.append(node.topRight)
            queue.append(node.bottomLeft)
            queue.append(node.bottomRight)

    return result


grid = [ [[0, 1], [1, 0]], [[1,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0], [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [1,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0]] ]

for test in range(len(grid)):
    root = constructQuadTree(grid[test])
    print(
        colored(f"Test {(test + 1)}:", "green"),
        serialize(root),
        " | ",
        colored("Passed", "green")
    )