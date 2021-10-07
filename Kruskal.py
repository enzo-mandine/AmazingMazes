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

def checkNodes(x, y, board):
    nodes = []
    size = range(len(board))
    N = y + 1
    S = y - 1
    E = x + 1
    W = x - 1
    if N in size:
        nodes.append([x, N])
    if S in size:
        nodes.append([x, S])
    if E in size:
        nodes.append([E, y])
    if W in size:
        nodes.append([W, y])

    return nodes


v = []
size = int(input('size :'))
visited = [[0 for i in range(0, size)] for j in range(0, size)]

for i in range(size):
    v.append([])
    for j in range(size):
        v[i].append(checkNodes(i, j, visited))
        print v[i][j]
