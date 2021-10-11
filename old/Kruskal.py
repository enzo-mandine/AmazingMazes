import random


class Room:
    def __init__(self, y, x, idx, size):
        self.x = y
        self.y = x
        self.idx = idx
        self.size = size
        self.connected = []
        self.isWall = {'n': True, 's': True, 'e': True, 'w': True}
        self.neighbours = None

    def openWall(self, position):
        if position == (self.x, self.y - 1):
            self.isWall['n'] = False
        if position == (self.x, self.y + 1):
            self.isWall['s'] = False
        if position == (self.x + 1, self.y):
            self.isWall['e'] = False
        if position == (self.x - 1, self.y):
            self.isWall['w'] = False

    def setNeighbours(self, matrix):
        nodes = []
        N = self.y - 1
        S = self.y + 1
        E = self.x + 1
        W = self.x - 1
        if N in range(0, self.size):
            nodes.append(matrix[self.x][N])
        if S in range(0, self.size):
            nodes.append(matrix[self.x][S])
        if E in range(0, self.size):
            nodes.append(matrix[E][self.y])
        if W in range(0, self.size):
            nodes.append(matrix[W][self.y])

        self.neighbours = nodes
        return True

    def getPosition(self):
        return self.x, self.y


mat = []
allRooms = []
size = int(input('dimension:'))

n = 0
for i in range(0, size):
    mat.append([])
    for j in range(0, size):
        newRoom = Room(i, j, n, size)
        allRooms.append(newRoom)
        mat[i].append(newRoom)
        n += 1

sets = []
walls = []
for i in range(0, size):
    for j in range(0, size):
        node = mat[i][j]
        node.setNeighbours(mat)
        sets.append({(int(node.x), int(node.y))})
        for neighbour in node.neighbours:
            wall = (node.x, node.y, neighbour.x, neighbour.y)
            llaw = [neighbour.x, neighbour.y, node.x, node.y]
            # print 'wall:', wall, 'llaw:', llaw
            if wall not in walls and llaw not in walls:
                walls.append(wall)

# print'sets', sets
walls_copy = walls[:]
random.shuffle(walls_copy)

for wall in walls_copy:
    set_a = None
    set_b = None

    for i in sets:
        # print 'set:', i, "walls:", wall[0], wall[1]
        if (wall[0], wall[1]) in i:
            # print 'in 0 1'
            set_a = i
        # try:
        if (wall[2], wall[3]) in i:
            # print 'in 2 3'
            set_b = i
        # except IndexError:
        #     print wall[2], wall[3]

    # print 'a:', set_a, 'b:', set_b
    if set_a is not set_b:
        sets.remove(set_a)
        sets.remove(set_b)
        sets.append(set_a.union(set_b))
        walls.remove(wall)

print walls

# print sets, '\n'
# print walls, '\n'

# for i in range(0, size):
#     for j in range(0, size):
#         print mat[i][j].idx, mat[i][j].getPosition(), mat[i][j].isWall
