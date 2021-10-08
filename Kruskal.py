# coding=utf-8

# 1) create a forest F (a set of trees), where each vertex in the graph is a separate tree
# 2) create a set S containing all the edges in the graph
# 3) while S is nonempty and F is not yet spanning
# 4)    remove an edge with minimum weight from S
# 5)    if the removed edge connects two different trees then add it to the forest F,
#       combining two trees into a single tree

# At the termination of the algorithm,
# the forest forms a minimum spanning forest of the graph.
# If the graph is connected, the forest has a single component and forms a minimum spanning tree.

# algorithm Kruskal(G) is
#     F:= ∅
#     for each v ∈ G.V do
#         MAKE-SET(v)
#     for each (u, v) in G.E ordered by weight(u, v), increasing do
#         if FIND-SET(u) ≠ FIND-SET(v) then
#             F:= F ∪ {(u, v)} ∪ {(v, u)}
#             UNION(FIND-SET(u), FIND-SET(v))
#     return F

# Give a unique subset id for each existing cell.
# Throw all of the edges into a big set.
# While there is an edge of being handled in the set:
# 1. Pull out one edge at random.
# 2. If the edge connects two disjoint subsets:
# a. Connect cells.
# b. Join the subsets.
import random


def checkNodes(x, y, board):
    nodes = []
    size = range(len(board))
    N = y + 1
    S = y - 1
    E = x + 1
    W = x - 1
    if N in size:
        nodes.append((x, N))
    if S in size:
        nodes.append((x, S))
    if E in size:
        nodes.append((E, y))
    if W in size:
        nodes.append((W, y))

    return nodes


size = int(input('dimension:'))
mat = []
m = {i: [] for i in range(0, size * size)}

print(m)

# edges = []
# size = int(input('size :'))
# m = [[0 for i in range(0, size)] for j in range(0, size)]
# ids = {}
# n = 0
# for i in range(size):
#     ids.update({n: []})
#     for j in range(size):
#         data = checkNodes(i, j, m)
#         prep = []
#         for e in data:
#             v = (i, j), e
#             prep.append(((i, j), e))
#             edges.append(((i, j), e))
#
#         ids[n] = prep
#         n += 1
#
# for row in ids.items():
#     selected = edges.pop(random.randrange(0, len(edges)))
#     for cell in row[1]:
#         for item in selected:
#             if item in cell:
#                 print(selected, cell)
# print('cell:', row[0], 'neighbours:', row[1])

# print edges
# vectorList = []
# for row in bag:
#     for vector in row:
#         vectorList.append(vector)
#
# maze = []
# maze.append([vectorList[0]])
# vectorList = vectorList[1:-1]
# result = []
# k = 0
# for vector in vectorList:
#     result.append([])
#     first = (vector[0][0], vector[0][1])
#     second = (vector[1][0], vector[1][1])
#     i = 0
#     for road in maze:
#         j = 0
#         for part in road:
#             # print part[j]
#             if first in part:
#                 print 'first:', first, 'vector:', vector, 'part:', part, 'road:', road
#                 maze.append(vector)
#                 print 'first:', first, 'vector:', vector, 'part:', part, 'road:', road
#             if second in part:
#                 print 'second:', second, 'vector:', vector, 'part:', part, 'road:', road
#                 # print 'first vector:', vector, 'road:', road, 'maze:', maze[i]
#         j += 1
#     i += 1
#     vectorList.pop(k)
# k += 1
#
# for row in result:
#     if len(row):
#         for a in row: print(a)
#
# for row in maze: print(row)
