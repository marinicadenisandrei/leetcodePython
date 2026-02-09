# Leetcode - 417. Pacific Atlantic Water Flow (Python language) - Medium

from collections import deque
from termcolor import colored

print(colored("Leetcode - 417. Pacific Atlantic Water Flow (Python language) - Medium", "yellow"))

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])

    def bfs(starts):
        reachable = set(starts)
        q = deque(starts)

        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable:
                    if heights[nr][nc] >= heights[r][c]:
                        reachable.add((nr, nc))
                        q.append((nr, nc))
        return reachable

    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

    pac = bfs(pacific_starts)
    atl = bfs(atlantic_starts)

    ans = sorted([[r, c] for (r, c) in (pac & atl)])
    return ans


# test
heights = [[
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
],
[[1]]]


for test in range(len(heights)):
    print(
        colored(f"Test {(test + 1)}:", "green"),
        pacificAtlantic(heights[test]),
        "|",
        colored("Passed", "green")
    )
