import sys
from random import shuffle

# set recursion limit
sys.setrecursionlimit(15000)


# The depth-first search algorithm of maze generation is frequently implemented using backtracking.
# This can be described with a following recursive routine:
# 1) Given a current cell as a parameter,
# 2) Mark the current cell as visited
# 3) While the current cell has any unvisited neighbour cells
# 4)        Choose one of the unvisited neighbours
# 5)        Remove the wall between the current cell and the chosen cell
# 6)        Invoke the routine recursively for a chosen cell

# which is invoked once for any initial cell in the area.


def checkNodes(x, y, board):
    nodes = []
    size = range(len(board))
    N, S, E, W = y + 1, y - 1, x + 1, x - 1

    if N in size:
        nodes.append([x, N])
    if S in size:
        nodes.append([x, S])
    if E in size:
        nodes.append([E, y])
    if W in size:
        nodes.append([W, y])

    return nodes


# 1) Given a current cell as a parameter,
def walk(x, y):
    # 2) Mark the current cell as visited
    visited[y][x] = 1

    # 3) While the current cell has any unvisited neighbour cells
    d = checkNodes(x, y, visited)
    shuffle(d)
    # print(d)
    # 4) Choose one of the unvisited neighbours
    for (xx, yy) in d:
        if visited[yy][xx] == 1:
            continue

        # 5) Remove the wall between the current cell and the chosen cell
        if xx == x:
            horizontal[max(y, yy)][x] = "#.."
        if yy == y:
            vertical[y][max(x, xx)] = "..."

        # 6) Invoke the routine recursively for a chosen cell
        walk(xx, yy)


# print the maze
def make_maze(x, y):
    walk(x, y)
    s = ""
    for (a, b) in zip(horizontal, vertical):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


size = int(input('size :'))

visited = [[0 for i in range(0, size)] for j in range(0, size)]
vertical = [["#.."] * size + ['#'] for _ in range(size)] + [[]]
vertical[0][0] = '...'
vertical[-2][-1] = '.'
horizontal = [["###"] * size + ['#'] for _ in range(size + 1)]
horizontal[0][0] = '..#'
horizontal[-1][-1] = '.'
horizontal[-1][-2] = '##.'

print(make_maze(0, 0))
for row in visited:
    for col in row:
        print(col)