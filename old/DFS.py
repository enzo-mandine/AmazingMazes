# The depth-first search algorithm of maze generation is frequently implemented using backtracking.
# This can be described with a following recursive routine:
# 1) Given a current cell as a parameter,
# 2) Mark the current cell as visited
# 3) While the current cell has any unvisited neighbour cells
# 4)        Choose one of the unvisited neighbours
# 5)        Remove the wall between the current cell and the chosen cell
# 6)        Invoke the routine recursively for a chosen cell

# which is invoked once for any initial cell in the area.


# size = int(input('enter integer: '))
from random import randrange, shuffle
from Room import *


def makeBoard():
    return [[Room(i, j) for i in range(0, size)] for j in range(0, size)]


def printBoard(maze):
    m = []
    for i in range(0, 5):
        m.append([])
        for j in range(0, 5):
            m[i].append([])
            m[i][j] = maze[i][j].getIsVisited()
    for row in m:
        print(row)
    print '\n'


def checkNodes(x, y, board):
    nodes = []
    N = y + 1
    S = y - 1
    E = x + 1
    W = x - 1
    if N <= size - 1:
        if not board[N][x].getIsVisited():
            nodes.append([x, N])
    if S >= 0:
        if not board[S][x].getIsVisited():
            nodes.append([x, S])
    if E <= size - 1:
        if not board[y][E].getIsVisited():
            nodes.append([E, y])
    if W >= 0:
        if not board[y][W].getIsVisited():
            nodes.append([W, y])

    return nodes


# function RouletteSelect(src) {
#     const roll = Math.random() * src.length;
#     let sum = 0;
#     for (let i = 0; i < src.length; i++) {
#       sum += 1.0;
#       if (roll < sum) {
#         const res = src[i];
#         src = src.splice(i, 1);
#         return res;
#       }
#     }
#   }

def filter(src):
    roll = random.random() * len(src)
    sum = 0
    for i in range(0, len(src)):
        sum += 1.0
        if roll < sum:
            res = src[i]
            src = src[i:1]
            return res


def resolve(x, y, maze):
    visited.append((x, y))
    neighbours = checkNodes(x, y, maze)
    node = maze[x][y]
    node.setIsVisited(True)
    printBoard(maze)
    shuffle(neighbours)
    for (xx, yy) in neighbours:
        print maze[yy][xx]


# while len(neighbours) - 1 > 0:
#     rand = neighbours[randrange(len(neighbours))]
#     selected = maze[rand[0]][rand[1]]
#     # print x, y, selected.x, selected.y, selected.visited
#     if (rand[0], rand[1]) not in visited:
#         return resolve(selected.x, selected.y, maze)


# _ProcessNode(nodeKey) {
#         this._visited[nodeKey] = true;
#         const node = this._nodes[nodeKey];
#         const neighbours = [...node.potentialEdges];
#         while (neighbours.length > 0) {
#           const ki = RouletteSelect(neighbours);
#           if (!(ki in this._visited)) {
#             const adjNode = this._nodes[ki];
#             node.edges.push(ki);
#             adjNode.edges.push(nodeKey);
#             this._ProcessNode(ki);
#           }
#         }
#       }

size = 5
visited = []
start = (0, 0)
maze = makeBoard()

# print 'checkNodes', start[0], start[0], ':', checkNodes(start[0], start[0], maze)
# print 'Board:'
resolve(0, 0, maze)
# print 'visited', visited

#
# # 1) Given a current cell as a parameter
# def carve(x, y):
#     # 2) Mark the current cell as visited
#     board[x][y].setIsVisited(True)
#     neighbours = []
#     direction = []
#
#     if y + 1 <= size - 1:
#         if not board[x][y + 1].getIsVisited():
#             neighbours.append(board[x][y + 1].getIsVisited())
#             direction.append([x, y + 1])
#
#     if y - 1 >= 0:
#         if not board[x][y - 1].getIsVisited():
#             neighbours.append(board[x][y - 1].getIsVisited())
#             direction.append([x, y - 1])
#
#     if x + 1 <= size - 1:
#         if not board[x + 1][y].getIsVisited():
#             neighbours.append(board[x + 1][y].getIsVisited())
#             direction.append([x + 1, y])
#
#     if x - 1 >= 0:
#         if not board[x - 1][y].getIsVisited():
#             neighbours.append(board[x - 1][y].getIsVisited())
#             direction.append([x - 1, y])
#
#     if not len(direction):
#         return
#
#     rand = random.randrange(0, len(direction))
#     # 3) While the current cell has any unvisited neighbour cells
#     while False in neighbours:
#         # 4)        Choose one of the unvisited neighbours
#         x = direction[rand][0]
#         y = direction[rand][1]
#         if not board[x][y].getIsVisited():
#             neighbours[rand] = True
#             # 5)        Remove the wall between the current cell and the chosen cell
#
#             # 6)        Invoke the routine recursively for a chosen cell
#             return carve(x, y)
#
#
# def possibleNeighbours():
#     pass
#
#
# carve(0, 0)
# result = []
# for i in range(len(board) - 1):
#     result.append([])
#     for j in range(len(board[0]) - 1):
#         result[i].append(board[i][j].getIsVisited())
#
# for row in result:
#     print row
